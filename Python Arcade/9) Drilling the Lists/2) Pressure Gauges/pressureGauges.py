def pressureGauges(morning, evening):
    return [map(min,zip(morning, evening)), map(max, zip(morning, evening))]