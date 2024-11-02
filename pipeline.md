```mermaid
%%{ init: { 'flowchart': { 'curve': 'monotoneX' } } }%%
graph LR;
meteo-weather-data[fa:fa-rocket meteo-weather-data &#8205] --> meteo-weather-chennai-raw{{ fa:fa-arrow-right-arrow-left meteo-weather-chennai-raw &#8205}}:::topic;
meteo-weather-chennai-raw{{ fa:fa-arrow-right-arrow-left meteo-weather-chennai-raw &#8205}}:::topic --> consume-meteo-weather-data[fa:fa-rocket consume-meteo-weather-data &#8205];
consume-meteo-weather-data[fa:fa-rocket consume-meteo-weather-data &#8205] --> bronze-weather-data-chennai{{ fa:fa-arrow-right-arrow-left bronze-weather-data-chennai &#8205}}:::topic;


classDef default font-size:110%;
classDef topic font-size:80%;
classDef topic fill:#3E89B3;
classDef topic stroke:#3E89B3;
classDef topic color:white;
```