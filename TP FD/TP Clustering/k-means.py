import numpy as np
import matplotlib.pyplot as plt


def Euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


def KmeansAmeliorer(points, threshold):
    global distances
    assigned_indices = []
    unassigned_points = []

    centroids = [points[np.random.randint(len(points))]]  # Choose a random point as the first centroid
    clusters = np.zeros(len(points))
    current_cluster = 1

    for i, point in enumerate(points):
        distances = [Euclidean_distance(point, centroid) for centroid in centroids]
        if min(distances) <= threshold:
            clusters[i] = current_cluster
            assigned_indices.append(i)

    # plot resultat
    plt.scatter(points[:, 0], points[:, 1], c=clusters, cmap='viridis')  # donner au clusters diff colors
    plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], c='red', marker='*', s=50)  # les centroids
    plt.show()

    while True:

        # plot resultat
        plt.scatter(points[:, 0], points[:, 1], c=clusters, cmap='viridis')  # donner au clusters diff colors
        plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], c='red', marker='*', s=50)  # les centroids
        plt.show()

        for i, point in enumerate(points):
            distances = [Euclidean_distance(point, centroid) for centroid in centroids]
            if min(distances) <= threshold:
                clusters[i] = current_cluster
                assigned_indices.append(i)

        # clusters.append(assigned_indices)

        if len(assigned_indices) == len(points) - 1:  # All points are assigned to clusters
            break

        # nv centroid parmi les non-assignés
        unassigned_points = np.delete(points, assigned_indices, axis=0)
        list_ = [np.max([Euclidean_distance(unassigned_points, centroid) for centroid in centroids]) for point in
                 points[clusters == 0]]
        if len(list_) != 0:
            new_centroid_idx = np.argmin(list_)
            new_centroid = points[clusters == 0][new_centroid_idx]
            centroids.append(new_centroid)
            current_cluster += 1
        else:
            break

        if threshold != min(distances):
            threshold = threshold - 0.1 * threshold

    return clusters, centroids


# random data
n = np.random.randint(100, 1000)
np.random.seed(n)
points = np.random.randn(50, 2)  # 2D points

# plot resultat
plt.scatter(points[:, 0], points[:, 1])
plt.show()

# application
clusters, centroids = KmeansAmeliorer(points, threshold=0.9)

# plot resultat
plt.scatter(points[:, 0], points[:, 1], c=clusters, cmap='viridis')  # donner au clusters diff colors
plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], c='red', marker='*', s=50)  # les centroids
plt.show()
