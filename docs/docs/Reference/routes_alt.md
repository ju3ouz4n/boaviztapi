## Impacts routes

The impact routes are used to retrieve the impacts of a given usage and configuration for a given asset. They represent the main feature of the API.

### Query parameters

They all have the same query parameters. If no query parameters are provided, the default values will be used.

| Parameter         | Description                                                                                                                                        | Default                                                               | Example                        |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|--------------------------------|
| ```criteria```    | List the impact criteria you want the API to compute .All impacts criteria can be found here ```/v1/utils/impact_criteria```                       | ```criteria=gwp&criteria=pe&criteria=adp```                           | ```criteria=gwp```             |
| ```verbose```     | If set at true, the API will detail the data used in the assessment. See [verbose](../Explanations/verbose.md).                                    | ```verbose=true```                                                    | ```verbose=false```            |
| ```archetype```   | The missing data will be completed from the chosen archetype. **Not implemented for cloud routes**. See [archetype](../Explanations/archetypes.md) | Default archetype for each asset can be set in the configuration file | ```archetype=compute_medium``` |
| ```duration```    | Duration considered for the assessment. If not provided, the total duration (lifetime) of the asset will be used.                                  | None                                                                  | ```duration=8760``` (1 year)   |

### GET

Requesting the route with a GET method will return the impacts with the values taken from the archetype.

|Method|           Routes          |         Description         |
|------|---------------------------|-----------------------------|
|  GET |        /v1/server/        |   Server Impact From Model  |
|  GET |     /v1/cloud/instance    |    Instance Cloud Impact    |
|  GET |    /v1/terminal/laptop    |        Laptop Impact        |
|  GET |    /v1/terminal/desktop   |        Desktop Impact       |
|  GET |  /v1/terminal/smartphone  |      Smartphone Impact      |
|  GET |    /v1/terminal/tablet    |        Tablet Impact        |
|  GET |  /v1/terminal/television  |      Television Impact      |
|  GET |      /v1/terminal/box     |          Box Impact         |
|  GET |   /v1/peripheral/monitor  |        Monitor Impact       |
|  GET |  /v1/peripheral/usb_stick |       Usb Stick Impact      |
|  GET |/v1/peripheral/external_ssd|     External Ssd Impact     |
|  GET |/v1/peripheral/external_hdd|     External Hdd Impact     |
|  GET |     /v1/component/cpu     |     Cpu Impact Bottom Up    |
|  GET |     /v1/component/ram     |     Ram Impact Bottom Up    |
|  GET |     /v1/component/ssd     |    Disk Impact Bottom Up    |
|  GET |     /v1/component/hdd     |    Disk Impact Bottom Up    |
|  GET | /v1/component/motherboard | Motherboard Impact Bottom Up|
|  GET | /v1/component/power_supply|Power Supply Impact Bottom Up|
|  GET |     /v1/component/case    |    Case Impact Bottom Up    |
|  GET |     /v1/iot/iot_device    |      Iot Device Impact      |
### POST

Requesting the route with a POST method will return the impacts with the values taken from the body. Missing values will be taken from the archetype or set by default.
The format section of the documentation details the format of the body for each route.

|Method|           Routes          |           Description          |
|------|---------------------------|--------------------------------|
| POST |        /v1/server/        |Server Impact From Configuration|
| POST |     /v1/cloud/instance    |      Instance Cloud Impact     |
| POST |    /v1/terminal/laptop    |          Laptop Impact         |
| POST |    /v1/terminal/desktop   |         Desktop Impact         |
| POST |  /v1/terminal/smartphone  |        Smartphone Impact       |
| POST |    /v1/terminal/tablet    |          Tablet Impact         |
| POST |  /v1/terminal/television  |        Television Impact       |
| POST |      /v1/terminal/box     |           Box Impact           |
| POST |   /v1/peripheral/monitor  |         Monitor Impact         |
| POST |  /v1/peripheral/usb_stick |        Usb Stick Impact        |
| POST |/v1/peripheral/external_ssd|       External Ssd Impact      |
| POST |/v1/peripheral/external_hdd|       External Hdd Impact      |
| POST |     /v1/component/cpu     |      Cpu Impact Bottom Up      |
| POST |     /v1/component/ram     |      Ram Impact Bottom Up      |
| POST |     /v1/component/ssd     |      Disk Impact Bottom Up     |
| POST |     /v1/component/hdd     |      Disk Impact Bottom Up     |
| POST | /v1/component/motherboard |  Motherboard Impact Bottom Up  |
| POST | /v1/component/power_supply|  Power Supply Impact Bottom Up |
| POST |     /v1/component/case    |      Case Impact Bottom Up     |
| POST |     /v1/iot/iot_device    |        Iot Device Impact       |
## Consumption profile routes

|Method|           Routes          |parameters|      Description      |
|------|---------------------------|----------|-----------------------|
| POST |/v1/consumption_profile/cpu|  verbose |Cpu Consumption Profile|
## Utils routes

Utils routes are used to retrieve the list of possible values for some parameters, to retrieve the list of archetypes for a given asset or to use some specific features.

|Method|                   Routes                   |      parameters      |            Description            |
|------|--------------------------------------------|----------------------|-----------------------------------|
|  GET |            /v1/server/archetypes           |                      |   Server Get All Archetype Name   |
|  GET |         /v1/server/archetype_config        |       archetype      |        Get Archetype Config       |
|  GET |     /v1/cloud/instance/instance_config     |provider instance_type|        Get Archetype Config       |
|  GET |      /v1/cloud/instance/all_instances      |       provider       |   Server Get All Archetype Name   |
|  GET |      /v1/cloud/instance/all_providers      |                      |    Server Get All Provider Name   |
|  GET |              /v1/terminal/all              |                      |    Terminal Get All Categories    |
|  GET |       /v1/terminal/laptop/archetypes       |                      |   Laptop Get All Archetype Name   |
|  GET |    /v1/terminal/laptop/archetype_config    |       archetype      |    Laptop Get Archetype Config    |
|  GET |       /v1/terminal/desktop/archetypes      |                      |   Desktop Get All Archetype Name  |
|  GET |    /v1/terminal/desktop/archetype_config   |       archetype      |    Desktop Get Archetype Config   |
|  GET |     /v1/terminal/smartphone/archetypes     |                      | Smartphone Get All Archetype Name |
|  GET |  /v1/terminal/smartphone/archetype_config  |       archetype      |  Smartphone Get Archetype Config  |
|  GET |       /v1/terminal/tablet/archetypes       |                      |   Tablet Get All Archetype Name   |
|  GET |    /v1/terminal/tablet/archetype_config    |       archetype      |    Tablet Get Archetype Config    |
|  GET |     /v1/terminal/television/archetypes     |                      | Television Get All Archetype Name |
|  GET |  /v1/terminal/television/archetype_config  |       archetype      |  Television Get Archetype Config  |
|  GET |         /v1/terminal/box/archetypes        |                      |     Box Get All Archetype Name    |
|  GET |      /v1/terminal/box/archetype_config     |       archetype      |      Box Get Archetype Config     |
|  GET |             /v1/peripheral/all             |                      |   Peripheral Get All Categories   |
|  GET |      /v1/peripheral/monitor/archetypes     |                      |   Monitor Get All Archetype Name  |
|  GET |   /v1/peripheral/monitor/archetype_config  |       archetype      |    Monitor Get Archetype Config   |
|  GET |     /v1/peripheral/usb_stick/archetypes    |                      |  Usb Stick Get All Archetype Name |
|  GET |  /v1/peripheral/usb_stick/archetype_config |       archetype      |   Usb Stick Get Archetype Config  |
|  GET |   /v1/peripheral/external_ssd/archetypes   |                      |External Ssd Get All Archetype Name|
|  GET |/v1/peripheral/external_ssd/archetype_config|       archetype      | External Ssd Get Archetype Config |
|  GET |   /v1/peripheral/external_hdd/archetypes   |                      |External Hdd Get All Archetype Name|
|  GET |/v1/peripheral/external_hdd/archetype_config|       archetype      | External Hdd Get Archetype Config |
|  GET |              /v1/component/all             |                      |       Cpu All Archetype Name      |
|  GET |         /v1/component/cpu/archetype        |                      |       Cpu All Archetype Name      |
|  GET |     /v1/component/cpu/archetype_config     |       archetype      |        Cpu Archetype Config       |
|  GET |         /v1/component/ram/archetype        |                      |       Ram All Archetype Name      |
|  GET |     /v1/component/ram/archetype_config     |       archetype      |        Ram Archetype Config       |
|  GET |         /v1/component/ssd/archetype        |                      |       Ssd All Archetype Name      |
|  GET |     /v1/component/ssd/archetype_config     |       archetype      |        Ssd Archetype Config       |
|  GET |         /v1/component/hdd/archetype        |                      |       Hdd All Archetype Name      |
|  GET |     /v1/component/hdd/archetype_config     |       archetype      |        Hdd Archetype Config       |
|  GET |     /v1/component/motherboard/archetype    |                      |   Motherboard All Archetype Name  |
|  GET | /v1/component/motherboard/archetype_config |       archetype      |    Motherboard Archetype Config   |
|  GET |    /v1/component/power_supply/archetype    |                      |  Power Supply All Archetype Name  |
|  GET | /v1/component/power_supply/archetype_config|       archetype      |   Power Supply Archetype Config   |
|  GET |        /v1/component/case/archetype        |                      |      Case All Archetype Name      |
|  GET |     /v1/component/case/archetype_config    |       archetype      |       Case Archetype Config       |
|  GET |        /v1/iot/iot_device/archetypes       |                      | Iot Device Get All Archetype Name |
|  GET |     /v1/iot/iot_device/archetype_config    |       archetype      |        Get Archetype Config       |
|  GET |              /v1/utils/version             |                      |              Version              |
|  GET |           /v1/utils/country_code           |                      |      Utils Get All Countries      |
|  GET |            /v1/utils/cpu_family            |                      |      Utils Get All Cpu Family     |
|  GET |          /v1/utils/cpu_model_range         |                      |   Utils Get All Cpu Model Range   |
|  GET |         /v1/utils/ssd_manufacturer         |                      |   Utils Get All Ssd Manufacturer  |
|  GET |         /v1/utils/ram_manufacturer         |                      |   Utils Get All Ram Manufacturer  |
|  GET |             /v1/utils/case_type            |                      |      Utils Get All Case Type      |
|  GET |            /v1/utils/name_to_cpu           |       cpu_name       |            Name To Cpu            |
|  GET |             /v1/utils/cpu_name             |                      |       Utils Get All Cpu Name      |
|  GET |          /v1/utils/impact_criteria         |                      |   Utils Get All Impacts Criteria  |
| GET    | /v1/utils/impact_criteria                    |                 | Get all available impact criteria  (name, code, description, unit)   |