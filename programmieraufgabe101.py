def roots(a, b, c, d, e, f):

    # die Funktion roots wird definiert mit den
    # benötigten Variablen

    n = 0                   # x hoch 5 immer positives Vorzeichen // Potenz: 5

    # n ist eine nette Variable zur Ermittlung der Vorzeichenwechsel

    if (a*d) >= 0:          # a mal b ist positiv / gleich null // Potenz: 4
        n += 0              # nichts wird zu n addiert -> n ist 0
    else:                   # a mal b ist negativ
        n += 1              # 1 wird zu n addiert -> n ist 1

    if (a*e+b*d) >= 0:      # () ist positiv / gleich null // Potenz: 3
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 0          # nichts wird zu n addiert -> n ist 0
        else:               # Vorzeichen war negativ
            n += 1          # 1 wird zu n addiert -> n ist 2
    else:                   # () ist negativ
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 1          # 1 wird zu n addiert -> n ist 1
        else:               # Vorzeichen war negativ
            n += 0          # nichts wird addiert -> n ist 1

    if (a*f+b*e+c*d) >= 0:  # () ist positiv / gleich null // Potenz: 2
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 0          # nichts wird zu n addiert -> n ist 0 oder 2
        else:               # Vorzeichen war negativ
            n += 1          # 1 wird zu n addiert -> n ist 2
    else:                   # () ist negativ
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 1          # 1 wird zu n addiert -> n ist 1 oder 3
        else:               # Vorzeichen war negativ
            n += 0          # nichts wird zu n addiert -> n ist 1

    if (b*f+c*e) >= 0:      # () ist positiv / gleich null // Potenz: 1
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 0          # nichts wird zu n addiert -> n ist 0 oder 2
        else:               # Vorzeichen war negativ
            n += 1          # 1 wird zu n addiert -> n ist 2 oder 4
    else:                   # () ist negativ
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 1          # 1 wird zu n addiert -> n ist 1 oder 3
        else:               # Vorzeichen war negativ
            n += 0          # nichts wird zu n addiert -> n ist 1 oder 3

    if (c*f) >= 0:          # () ist positiv / gleich null // Potenz: 0
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 0          # nichts wird zu n addiert -> n ist 0 oder 2 oder 4
        else:               # Vorzeichen war negativ
            n += 1          # 1 wird zu n addiert -> n ist 2 oder 4
    else:                   # () ist negativ
        if n % 2 == 0:      # Vorzeichen war positiv
            n += 1          # 1 wird zu n addiert -> n ist 1 oder 3 oder 5
        else:               # Vorzeichen war negativ
            n += 0          # nichts wird zu n addiert -> n ist 1 oder 3

    if n % 2 == 0:          # return für gerade Anzahl
        return "Das Polynom hat eine gerade Anzahl \
von positiven reellen Wurzeln."
    else:                   # return für ungerade Anzahl
        return "Das Polynom hat eine ungerade Anzahl \
von positiven reellen Wurzeln."
