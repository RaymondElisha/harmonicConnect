from collections import Counter


def match_clients_to_service_providers(client, service_providers):
    # Match based on event type, location, and genre compatibility
    matches = []

    for provider in service_providers:
        compatibility_score = calculate_compatibility(client, provider)
        matches.append({'provider': provider, 'score': compatibility_score})

    # Sort matches by compatibility score in descending order
    sorted_matches = sorted(matches, key=lambda x: x['score'], reverse=True)

    return sorted_matches


def calculate_compatibility(client, provider):
    # Calculate compatibility score based on event type, location, and genre
    event_type_score = 2 if client.event_set.last(
    ).event_type == provider.event_set.last().event_type else 0
    location_score = 2 if client.event_set.last(
    ).location == provider.event_set.last().location else 0
    genre_score = calculate_genre_similarity(client, provider)

    total_score = event_type_score + location_score + genre_score
    return total_score


def calculate_genre_similarity(client, provider):
    # Calculate genre similarity using Jaccard similarity coefficient
    client_genres = set(client.event_set.last().genres.split(','))
    provider_genres = set(provider.event_set.last().genres.split(','))

    intersection_len = len(client_genres.intersection(provider_genres))
    union_len = len(client_genres.union(provider_genres))

    if union_len == 0:
        return 0

    similarity_score = intersection_len / union_len
    return similarity_score
