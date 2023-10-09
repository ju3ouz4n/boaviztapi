import pytest
from httpx import AsyncClient

from boaviztapi.main import app

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_complete_config_server():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post('/v1/server/?verbose=false', json={
            "model": {
            },
            "configuration": {
                "cpu": {
                    "units": 2,
                    "core_units": 24,
                    "die_size_per_core": 24.5
                },
                "ram": [
                    {
                        "units": 4,
                        "capacity": 32,
                        "density": 1.79
                    },
                    {
                        "units": 4,
                        "capacity": 16,
                        "density": 1.79
                    }
                ],
                "disk": [
                    {
                        "units": 2,
                        "type": "ssd",
                        "capacity": 400,
                        "density": 50.6
                    },
                    {
                        "units": 2,
                        "type": "hdd"
                    }
                ],
                "power_supply": {
                    "units": 2,
                    "unit_weight": 10
                }
            }
        })
    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 0.2611,
                                                           'min': 0.2536,
                                                           'value': 0.2536,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 0.007799, 'min': 0.0001938, 'value': 0.0013}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 1140.0,
                                                           'min': 1075.0,
                                                           'value': 1140.0,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 26430.0, 'min': 337.7, 'value': 7000.0}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 15450.0,
                                                          'min': 14480.0,
                                                          'value': 15450.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation']},
                                             'unit': 'MJ',
                                             'use': {'max': 13750000.0,
                                                     'min': 190.9,
                                                     'value': 300000.0,
                                                     'warnings': [
                                                         'Uncertainty from technical characteristics is very important. '
                                                         'Results should be interpreted with caution (see '
                                                         'min and max values)']}}}}


@pytest.mark.asyncio
async def test_empty_config_server():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post('/v1/server/?verbose=false', json={})
    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 87.57,
                                                           'min': 0.05434,
                                                           'value': 0.2,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 0.07592, 'min': 8.849e-05, 'value': 0.002}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 3034000.0,
                                                           'min': 201.0,
                                                           'value': 3000.0,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 257300.0, 'min': 154.2, 'value': 10000.0}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 37660000.0,
                                                          'min': 2763.0,
                                                          'value': 40000.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation',
                                                                       'Uncertainty from technical characteristics is very '
                                                                       'important. Results should be interpreted '
                                                                       'with caution (see min and max values)']},
                                             'unit': 'MJ',
                                             'use': {'max': 133800000.0,
                                                     'min': 87.15,
                                                     'value': 300000.0,
                                                     'warnings': [
                                                         'Uncertainty from technical characteristics is very important. '
                                                         'Results should be interpreted with caution (see '
                                                         'min and max values)']}}}}


@pytest.mark.asyncio
async def test_dell_r740_server():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post('/v1/server/?verbose=false', json={
            "model":
                {
                    "name": "R740",
                    "type": "rack",
                    "year": 2020
                },
            "configuration":
                {
                    "cpu":
                        {
                            "units": 2,
                            "core_units": 24,
                            "die_size_per_core": 24.5
                        },
                    "ram":
                        [
                            {
                                "units": 12,
                                "capacity": 32,
                                "density": 1.79
                            }
                        ],
                    "disk":
                        [
                            {
                                "units": 1,
                                "type": "ssd",
                                "capacity": 400,
                                "density": 50.6
                            }
                        ],
                    "power_supply":
                        {
                            "units": 2,
                            "unit_weight": 2.99
                        }
                },
            "usage": {
            }
        })

    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 0.1492,
                                                           'min': 0.1492,
                                                           'value': 0.1492,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 0.008814, 'min': 0.000219, 'value': 0.0014}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 969.8,
                                                           'min': 969.8,
                                                           'value': 969.8,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 29870.0, 'min': 381.6, 'value': 8000.0}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 12900.0,
                                                          'min': 12900.0,
                                                          'value': 12900.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation']},
                                             'unit': 'MJ',
                                             'use': {'max': 15540000.0,
                                                     'min': 215.7,
                                                     'value': 300000.0,
                                                     'warnings': [
                                                         'Uncertainty from technical characteristics is very important. '
                                                         'Results should be interpreted with caution (see '
                                                         'min and max values)']}}}}


@pytest.mark.asyncio
async def test_partial_server_1():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post('/v1/server/?verbose=false', json={
            "model": {
            },
            "configuration": {
                "cpu": {
                    "units": 2
                },
                "ram": [
                    {
                        "units": 4,
                        "capacity": 32
                    },
                    {
                        "units": 4,
                        "capacity": 16
                    }
                ],
                "disk": [
                    {
                        "units": 2,
                        "type": "ssd"
                    },
                    {
                        "units": 2,
                        "type": "hdd"
                    }
                ]
            }
        })
    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 6.674,
                                                           'min': 0.1128,
                                                           'value': 0.2,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 0.007799, 'min': 0.0001938, 'value': 0.0013}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 225200.0,
                                                           'min': 1183.0,
                                                           'value': 1000.0,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 26430.0, 'min': 337.7, 'value': 7000.0}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 2796000.0,
                                                          'min': 14840.0,
                                                          'value': 20000.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation',
                                                                       'Uncertainty from technical characteristics is very '
                                                                       'important. Results should be interpreted '
                                                                       'with caution (see min and max values)']},
                                             'unit': 'MJ',
                                             'use': {'max': 13750000.0,
                                                     'min': 190.9,
                                                     'value': 300000.0,
                                                     'warnings': [
                                                         'Uncertainty from technical characteristics is very important. '
                                                         'Results should be interpreted with caution (see '
                                                         'min and max values)']}}}}


@pytest.mark.asyncio
async def test_partial_server_2():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post('/v1/server/?verbose=false', json={
            "model": {
            },
            "configuration": {
                "cpu": {
                    "units": 2,
                    "die_size": 24.5
                },
                "ram": [
                    {
                        "units": 4
                    },
                    {
                        "units": 4,
                        "capacity": 16,
                        "density": 1.79
                    }
                ],
                "disk": [
                    {
                        "units": 2,
                        "capacity": 400,
                        "density": 50.6,
                        "type": "ssd"
                    },
                    {
                        "units": 2,
                        "type": "hdd"
                    }
                ],
                "power_supply": {
                    "units": 2,
                    "unit_weight": 10
                }
            }
        })
    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 0.5086,
                                                           'min': 0.2493,
                                                           'value': 0.26,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 0.007799, 'min': 0.0001938, 'value': 0.0013}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 9902.0,
                                                           'min': 904.8,
                                                           'value': 1400.0,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 26430.0, 'min': 337.7, 'value': 7000.0}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 124300.0,
                                                          'min': 12340.0,
                                                          'value': 20000.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation']},
                                             'unit': 'MJ',
                                             'use': {'max': 13750000.0,
                                                     'min': 190.9,
                                                     'value': 300000.0,
                                                     'warnings': [
                                                         'Uncertainty from technical characteristics is very important. '
                                                         'Results should be interpreted with caution (see '
                                                         'min and max values)']}}}}


@pytest.mark.asyncio
async def test_partial_server_3():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post('/v1/server/?verbose=false', json={
            "model": {
            },
            "configuration": {

                "ram": [
                    {
                        "units": 4,
                        "capacity": 16,
                        "density": 1.79
                    }
                ],
                "power_supply": {
                    "units": 2,
                    "unit_weight": 10
                }
            }
        })
    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 79.3,
                                                           'min': 0.2193,
                                                           'value': 0.2,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 0.05461, 'min': 9.269e-05, 'value': 0.001}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 2752000.0,
                                                           'min': 754.8,
                                                           'value': 900.0,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 185000.0, 'min': 161.5, 'value': 10000.0}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 34160000.0,
                                                          'min': 10620.0,
                                                          'value': 10000.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation',
                                                                       'Uncertainty from technical characteristics is very '
                                                                       'important. Results should be interpreted '
                                                                       'with caution (see min and max values)']},
                                             'unit': 'MJ',
                                             'use': {'max': 96250000.0,
                                                     'min': 91.29,
                                                     'value': 200000.0,
                                                     'warnings': [
                                                         'Uncertainty from technical characteristics is very important. '
                                                         'Results should be interpreted with caution (see '
                                                         'min and max values)']}}}}


@pytest.mark.asyncio
async def test_custom_usage_1():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/v1/server/?verbose=false&duration=8785", json={
            "usage": {
                "avg_power": 1,
                "usage_location": "FRA"
            }
        })
    assert res.json() == {"impacts": {'adp': {'description': 'Use of minerals and fossil ressources',
                                              'embedded': {'max': 21.95,
                                                           'min': 0.01362,
                                                           'value': 0.06,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgSbeq',
                                              'use': {'max': 4.268e-07, 'min': 4.268e-07, 'value': 4.268e-07}},
                                      'gwp': {'description': 'Total climate change',
                                              'embedded': {'max': 760800.0,
                                                           'min': 50.4,
                                                           'value': 800.0,
                                                           'warnings': ['End of life is not included in the '
                                                                        'calculation',
                                                                        'Uncertainty from technical characteristics is very '
                                                                        'important. Results should be interpreted '
                                                                        'with caution (see min and max values)']},
                                              'unit': 'kgCO2eq',
                                              'use': {'max': 0.8609, 'min': 0.8609, 'value': 0.8609}},
                                      'pe': {'description': 'Consumption of primary energy',
                                             'embedded': {'max': 9442000.0,
                                                          'min': 692.6,
                                                          'value': 10000.0,
                                                          'warnings': ['End of life is not included in the '
                                                                       'calculation',
                                                                       'Uncertainty from technical characteristics is very '
                                                                       'important. Results should be interpreted '
                                                                       'with caution (see min and max values)']},
                                             'unit': 'MJ',
                                             'use': {'max': 99.17, 'min': 99.17, 'value': 99.17}}}}
