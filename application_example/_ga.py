from numba import njit, prange
import numpy as np

from ._tsp import TSP_DIST_MATRIX, TSP_N_CITIES


# ---- Genetic Algorithm (GA) and components ---- #
@njit
def _initialize_population(pop_size):
    """Initializes the population with random tours for the TSP."""
    pop = np.empty((pop_size, TSP_N_CITIES), dtype=np.int32)
    for i in range(pop_size):
        pop[i] = np.random.permutation(TSP_N_CITIES)
    return pop


@njit
def _tour_distance(tour):
    """Calculates the total distance of an individual tour."""
    # Calculate total distance for consecutive cities
    total_dist = 0.0
    for i in range(TSP_N_CITIES - 1):
        total_dist += TSP_DIST_MATRIX[tour[i], tour[i + 1]]

    # Add the return leg back to the starting city
    return total_dist + TSP_DIST_MATRIX[tour[-1], tour[0]]


@njit(parallel=True)
def _batch_distances(pop):
    """Calculates distances for tours in the population."""
    pop_size = len(pop)
    distances = np.empty(pop_size, dtype=np.float64)
    for i in prange(pop_size):
        distances[i] = _tour_distance(pop[i])
    return distances


@njit
def _rank_population(pop):
    """Ranks the population based on individual fitness of a tour."""
    distances = _batch_distances(pop)
    fitness = 1.0 / distances
    ranking_idx = np.argsort(fitness)[::-1]
    return pop[ranking_idx], fitness[ranking_idx]


@njit
def _selection(pop, fitness, tournament_size):
    """Executes a tournament to select a tour from the population."""
    # Sample individuals for the tournament
    pop_size = len(pop)
    sample_idx = np.random.choice(pop_size, tournament_size, replace=False)

    # Select the best individual sample
    best_idx = -1
    best_fit = -1e9
    for i in sample_idx:
        if fitness[i] > best_fit:
            best_fit = fitness[i]
            best_idx = i
    return pop[best_idx]


@njit
def _city_is_in_tour(city, tour):
    """Check if a city is present in a tour.

    While using `np.isin` could be more concise and readable, this
    function can be more performant and memory-efficient under Numba
    JIT compilation, as it avoids creating intermediate boolean arrays.
    """
    for i in range(len(tour)):
        if tour[i] == city:
            return True
    return False


@njit
def _crossover(parent1, parent2, crossover_rate):
    """Ordered crossover with probability to create a child tour"""
    # Return the first parent if no crossover is performed
    if np.random.rand() >= crossover_rate:
        return parent1.copy()

    # Select a random sequence from the first parent.
    start, end = sorted(np.random.choice(TSP_N_CITIES, 2, replace=False))
    child = np.full(TSP_N_CITIES, -1, dtype=parent1.dtype)
    child[start:end] = parent1[start:end]

    # Fill the remaining cities in order from the second parent.
    pos = end
    for city in parent2:
        if not _city_is_in_tour(city, child):
            while child[pos % TSP_N_CITIES] != -1:
                pos += 1
            child[pos % TSP_N_CITIES] = city
    return child


@njit
def _mutation(tour, mutation_rate):
    """Inversion mutation with probability to modify a tour."""
    if np.random.rand() < mutation_rate:
        i, j = sorted(np.random.choice(len(tour), 2, replace=False))
        tour[i : j + 1] = tour[i : j + 1][::-1]
    return tour


@njit
def genetic_algorithm(
    pop_size,
    elite_split,
    tournament_split,
    crossover_rate,
    mutation_rate,
    generations,
    seed=-1,
):
    """Genetic algorithm to solve a TSP instance with 100 cities."""
    # Optional seeding to reproduce results.
    if seed != -1:
        np.random.seed(seed)

    # Random initialization
    pop = _initialize_population(pop_size)

    # Evolution Loop
    elite_size = int(pop_size * elite_split)
    tournament_size = max(1, int(pop_size * tournament_split))
    for i in range(generations):

        # Ranking based on individual fitness
        pop, fitness = _rank_population(pop)

        # Selection of elite individuals
        offspring = np.empty_like(pop)
        offspring[:elite_size] = pop[:elite_size]

        # Selection and modification to fill the population
        for i in range(elite_size, pop_size):
            parent1 = _selection(pop, fitness, tournament_size)
            parent2 = _selection(pop, fitness, tournament_size)
            child = _crossover(parent1, parent2, crossover_rate)
            child = _mutation(child, mutation_rate)
            offspring[i] = child

        # Update population
        pop = offspring

    # Final ranking to select the best individual tour.
    pop, _ = _rank_population(pop)
    best_tour = pop[0]
    best_cost = _tour_distance(best_tour)
    return best_cost, best_tour
