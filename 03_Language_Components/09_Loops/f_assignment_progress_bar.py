"""
Purpose: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""

data_set = range(-100,10_00_000)
data_set_length = len(data_set)
star = "*"

for index, _ in enumerate(data_set):
    percent_completed = (index / data_set_length) * 100
    percent_completed = round(percent_completed, 2)
    percent_rounded = star * (int(percent_completed // 10))
    print(f"\r{percent_rounded:10}", end ="")

