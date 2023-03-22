import boaviztapi.utils.roundit as rd
from boaviztapi import config
from boaviztapi.model.boattribute import Boattribute
from boaviztapi.model.component.component import Component, ComputedImpacts
from boaviztapi.model.impact import ImpactFactor
from boaviztapi.service.archetype import get_component_archetype, get_arch_value


class ComponentPowerSupply(Component):
    NAME = "POWER_SUPPLY"

    IMPACT_FACTOR = {
        'gwp': {
            'impact': 24.30
        },
        'pe': {
            'impact': 352.00
        },
        'adp': {
            'impact': 8.30E-03
        }
    }

    def __init__(self, archetype=get_component_archetype(config["default_power_supply"], "power_supply"), **kwargs):
        super().__init__(archetype=archetype, **kwargs)

        self.unit_weight = Boattribute(
            unit="kg",
            default=get_arch_value(archetype, 'unit_weight', 'default'),
            min=get_arch_value(archetype, 'unit_weight', 'min'),
            max=get_arch_value(archetype, 'unit_weight', 'max')
        )

    def impact_manufacture_gwp(self) -> ComputedImpacts:
        return self.__impact_manufacture('gwp')

    def __impact_manufacture(self, impact_type: str) -> ComputedImpacts:
        impact_factor = ImpactFactor(
            value=self.IMPACT_FACTOR[impact_type]['impact'],
            min=self.IMPACT_FACTOR[impact_type]['impact'],
            max=self.IMPACT_FACTOR[impact_type]['impact']
        )

        impact = self.__compute_impact_manufacture(impact_factor)
        sign_figures = rd.min_significant_figures(impact_factor.value)

        return impact.value, sign_figures, impact.min, impact.max, []

    def __compute_impact_manufacture(self, power_supply_impact: ImpactFactor) -> ImpactFactor:
        return ImpactFactor(
            value=self.unit_weight.value * power_supply_impact.value,
            min=self.unit_weight.min * power_supply_impact.min,
            max=self.unit_weight.max * power_supply_impact.max
        )

    def impact_manufacture_pe(self) -> ComputedImpacts:
        return self.__impact_manufacture('pe')

    def impact_manufacture_adp(self) -> ComputedImpacts:
        return self.__impact_manufacture('adp')

    def impact_use_gwp(self, model=None) -> ComputedImpacts:
        raise NotImplementedError

    def impact_use_pe(self, model=None) -> ComputedImpacts:
        raise NotImplementedError

    def impact_use_adp(self, model=None) -> ComputedImpacts:
        raise NotImplementedError
