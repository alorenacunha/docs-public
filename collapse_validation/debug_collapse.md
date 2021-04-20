# Validação Collapse

O objetivo deste arquivo é registrar validação ponto a ponto no cálculo de colapso.
"Original" - código disponibilizado pelo Pedro e Versiani
"Plataforma" - código implementado e integrado na plataforma Quality
Para realizar essa validação foi utilizado os arquivos de dados em anexo:

- [WT_data_condensed_wt.xlsx](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/WT_data_condensed.xlsx)
- [OD_data_condensed_od.xlsx](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/OD_data_condensed.xlsx)

## Método de validação:

1. Leitura e verificação de arquivos:

- Ler arquivos nos códigos 'original' versão do Versiani e executar o verify_pipe realizando as conversões de unidade
- Ler arquivos na plataforma realizando as conversões de unidade e executando o verify_pipe na plataforma
- Comparar valores de saída original vs plataforma

2. Execução do modelo de colapso:

- Rodar o modelo de colapso com valores sugeridos na versão original
- Executar o valor de colapso com os mesmo parâmetros de entrada na plataforma
- Comparar valores de colapso de saída original vs plataforma

3. Executar as mesmas etapas anteriores com os arquivos Muskogee (Rafael Braga)

### Leitura e verificação de arquivos

1. Ler arquivos nos códigos 'original' versão do Versiani e executar o verify_pipe realizando as conversões de unidade

```python

    # create the units dictionary
    dict_units = {"position_WT": "in", #unit
                  "position_OD" : "ft",
                  "WT" : "in",
                  "OD" : "mm",
                  "blind_length_end_OD" : "mm",
                  "blind_length_end_WT" : "mm",
                  "drift_length" : "mm",
                  "min_pipe_length" : "mm",
                  "max_pipe_length" : "mm",
                  "cut_off_length" : "mm",
                  "WTnom" : "in",
                  "ODnom" : "mm",
                  "output_position":"mm",
                  "output_WT":"mm",
                  "output_OD":"mm"}

    #body
    body_dict = {"input" : {
                    "df_segments_OD": data_od.to_dict('record'),
                    "df_segments_WT" : data_wt.to_dict('record'),
                    "blind_length_end_WT" : 300,
                    "blind_length_end_OD" : 300,
                    "averaging_length_collapse" : averaging_length_collapse,
                    "drift_length" : 300,
                    "min_pipe_length" : 11580,
                    "max_pipe_length" : 13720,
                    "cut_off_length" : 100,
                    "od_limit_min" : -0.5,
                    "od_limit_max" : 1,
                    "RBW" : 0.9,
                    "WTnom" : 0.82,
                    "ODnom" : 357,
                    "dict_units" : dict_units}
                  }


```

- [verify_pipe_original.xlsx](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/verify_pipe_original.xlsx)

2. Ler arquivos na plataforma realizando as conversões de unidade e executando o verify_pipe na plataforma

- Configuração de Projeto:
  
  ![projeto_information](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/project_information.png?raw=true)

  ```json
  {
    "id": 67,
    "dth_created_reg": "2021-04-14T00:08:44.992Z",
    "dth_updated_reg": "2021-04-16T20:26:46.713Z",
    "project_name": "condensed 2",
    "mill_order": null,
    "mill": "vsb",
    "customer": null,
    "customer_order": null,
    "collapse_rating": 10300.0,
    "collapse_rating_unit": "psi",
    "cut_off": 100.0,
    "cut_off_unit": "mm",
    "grade": "13CRSS",
    "rbw": 0.9,
    "drift": 300,
    "drift_unit": "mm",
    "input_range": "Custom",
    "range_unit": "mm",
    "range_min": 11580.0,
    "range_max": 13720.0,
    "averaging_length_collapse": 4,
    "od_nom": 357.0,
    "od_unit": "mm",
    "od_min": 0,
    "od_min_unit": "%",
    "od_max": 1,
    "od_max_unit": "%",
    "od_blind": 300,
    "od_blind_unit": "mm",
    "wt_nom": 0.82,
    "wt_unit": "in",
    "wt_blind": 300,
    "wt_blind_unit": "mm",
    "output_dimension_unit": "mm",
    "output_pressure_unit": "psi",
    "upload_pipes_status": "checked",
    "verify_pipe_status": "checked",
    "data_laboratory_status": "checked",
    "collapse_calculation_status": "current",
    "end_cropping_status": "able",
    "report_status": "disabled",
    "requests": [
      {
        "description": "WT_data_condensed_wt.xlsx, OD_data_condensed_od.xlsx",
        "functionName": "assignMetadata",
        "type": "upload.data",
        "id": "0b9c6b1c-9fbd-4c06-8e9a-398462099b56",
        "payload": { "uuid": "0b9c6b1c-9fbd-4c06-8e9a-398462099b56", "od_unit": "mm", "od_position_unit": "ft", "wt_unit": "in", "wt_position_unit": "in" },
        "stage": "upload_pipes_status",
        "status": "COMPLETED",
        "count": 5,
        "error": null
      }
    ],
    "collapse_rating_premium_unit": "psi",
    "pfs": null,
    "collapse_rating_premium": 10300.0
  }
  ```

- Arquivos com unidades convertidas na plataforma

  - [od_platform.csv](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/od_platform.csv)
  - [wt_platform.csv](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/wt_platform.csv)

- Verify Pipe
  - [warnings_original](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/warnings_original.xlsx)
  - [warnings_platform](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/warnings_platform.csv)
  - [verify_pipe_original](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/verify_pipe_original.xlsx)
  - [verify_pipe_platform](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/verify_pipe_platform.csv)

1. Comparar valores de saída original vs plataforma

- #### Comparativo de warnings

  - DB2397 XX 31

    - original

    ```json
    {
      "duplic_inspec_OD": false,
      "duplic_inspec_WT": false,
      "empty_values_ODODmin": false,
      "empty_values_ODODavg": false,
      "empty_values_ODODmax": false,
      "empty_values_WTWTmin": false,
      "empty_values_WTWTavg": false,
      "empty_values_WTWTmax": false,
      "short_pipe": true,
      "long_pipe": false,
      "wtminWTmin": false,
      "wtminWTmin_segment": null,
      "odminODmin": false,
      "odminODmin_segment": null,
      "odmaxODmax": true,
      "odmaxODmax_segment": "[ 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0, 7300.0, 7400.0, 7500.0, 7600.0, 7700.0, 7800.0, 7900.0, 8000.0, 8100.0, 8200.0, 8300.0, 8400.0, 8500.0, 8600.0, 8700.0, 8800.0, 8900.0, 9000.0, 9100.0, 9200.0, 9300.0, 9400.0, 9500.0, 9600.0, 9700.0, 9800.0, 9900.0, 10000.0, 10100.0, 10200.0, 10300.0, 10400.0, 10500.0, 10600.0]",
      "repeat_measurWTmin": false,
      "repeat_measurWTavg": false,
      "repeat_measurWTmax": false,
      "repeat_measurODmin": false,
      "repeat_measurODavg": false,
      "repeat_measurODmax": false,
      "ab_ovov": false,
      "ab_ovov_segment": null,
      "ab_eccecc": false,
      "ab_eccecc_segment": null,
      "ab_WTminWTmin": false,
      "ab_WTminWTmin_segment": null,
      "max_pitch_OD": false,
      "max_pitch_WT": false
    }
    ```

    - platform

    ````json
     {
        "duplic_inspec_OD": false,
        "duplic_inspec_WT": false,
        "empty_values_ODODmin": false,
        "empty_values_ODODavg": false,
        "empty_values_ODODmax": false,
        "empty_values_WTWTmin": false,
        "empty_values_WTWTavg": false,
        "empty_values_WTWTmax": false,
        "short_pipe": true,
        "long_pipe": false,
        "wtminWTmin": false,
        "wtminWTmin_segment": null,
        "odminODmin": false,
        "odminODmin_segment": null,
        "odmaxODmax": true,
        "odmaxODmax_segment": "[600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0,9100.0,9200.0,9300.0,9400.0,9500.0,9600.0,9700.0,9800.0,9900.0,10000.0,10100.0,10200.0,10300.0,10400.0,10500.0,10600.0,10700.0,10800.0,10900.0]",
        "repeat_measurWTmin": false,
        "repeat_measurWTavg": false,
        "repeat_measurWTmax": false,
        "repeat_measurODmin": false,
        "repeat_measurODavg": false,
        "repeat_measurODmax": false,
        "ab_ovov": false,
        "ab_ovov_segment": null,
        "ab_eccecc": false,
        "ab_eccecc_segment": null,
        "ab_WTminWTmin": false,
        "ab_WTminWTmin_segment": null,
        "max_pitch_OD": false,
        "max_pitch_WT": false
      }

    ```

  - DB2397 XX 22

    - original
    

    ```json
    {
      "duplic_inspec_OD": false,
      "duplic_inspec_WT": false,
      "empty_values_ODODmin": false,
      "empty_values_ODODavg": false,
      "empty_values_ODODmax": false,
      "empty_values_WTWTmin": false,
      "empty_values_WTWTavg": false,
      "empty_values_WTWTmax": false,
      "short_pipe": false,
      "long_pipe": false,
      "wtminWTmin": false,
      "wtminWTmin_segment": null,
      "odminODmin": false,
      "odminODmin_segment": null,
      "odmaxODmax": true,
      "odmaxODmax_segment": "[ 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0, 7300.0, 7400.0, 7500.0, 7600.0, 7700.0, 7800.0, 7900.0, 8000.0, 8100.0, 8200.0, 8300.0, 8400.0, 8500.0, 8600.0, 8700.0, 8800.0, 8900.0, 9000.0, 9100.0, 9200.0, 9300.0, 9400.0, 9500.0, 9600.0, 9700.0, 9800.0, 9900.0, 10000.0, 10100.0, 10200.0, 10300.0, 10400.0, 10500.0, 10600.0, 10700.0, 10800.0, 10900.0, 11000.0, 11100.0, 11200.0, 11300.0, 11400.0, 11500.0, 11600.0, 11700.0, 11800, 11900, 12000, 12100, 12200, 12300",
      "repeat_measurWTmin": false,
      "repeat_measurWTavg": false,
      "repeat_measurWTmax": false,
      "repeat_measurODmin": false,
      "repeat_measurODavg": false,
      "repeat_measurODmax": false,
      "ab_ovov": false,
      "ab_ovov_segment": null,
      "ab_eccecc": false,
      "ab_eccecc_segment": null,
      "ab_WTminWTmin": false,
      "ab_WTminWTmin_segment": null,
      "max_pitch_OD": false,
      "max_pitch_WT": false
    }
    ```

    - platforma`
    ```json
      {
        "duplic_inspec_OD": false,
        "duplic_inspec_WT": false,
        "empty_values_ODODmin": false,
        "empty_values_ODODavg": false,
        "empty_values_ODODmax": false,
        "empty_values_WTWTmin": false,
        "empty_values_WTWTavg": false,
        "empty_values_WTWTmax": false,
        "short_pipe": false,
        "long_pipe": true,
        "wtminWTmin": false,
        "wtminWTmin_segment": null,
        "odminODmin": false,
        "odminODmin_segment": null,
        "odmaxODmax": true,
        "odmaxODmax_segment": "[600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0,9100.0,9200.0,9300.0,9400.0,9500.0,9600.0,9700.0,9800.0,9900.0,10000.0,10100.0,10200.0,10300.0,10400.0,10500.0,10600.0,10700.0,10800.0,10900.0,11000.0,11100.0,11200.0,11300.0,11400.0,11500.0,11600.0,11700.0,11800.0,11900.0,12000.0,12100.0,12200.0,12300.0]",
        "repeat_measurWTmin": false,
        "repeat_measurWTavg": false,
        "repeat_measurWTmax": false,
        "repeat_measurODmin": false,
        "repeat_measurODavg": false,
        "repeat_measurODmax": false,
        "ab_ovov": false,
        "ab_ovov_segment": null,
        "ab_eccecc": false,
        "ab_eccecc_segment": null,
        "ab_WTminWTmin": false,
        "ab_WTminWTmin_segment": null,
        "max_pitch_OD": false,
        "max_pitch_WT": false
      }
      ```

  - DB2399 XX 54

    - original
    

    ```json
    {
      "duplic_inspec_OD": false,
      "duplic_inspec_WT": false,
      "empty_values_ODODmin": false,
      "empty_values_ODODavg": false,
      "empty_values_ODODmax": false,
      "empty_values_WTWTmin": false,
      "empty_values_WTWTavg": false,
      "empty_values_WTWTmax": false,
      "short_pipe": false,
      "long_pipe": false,
      "wtminWTmin": false,
      "wtminWTmin_segment": null,
      "odminODmin": false,
      "odminODmin_segment": null,
      "odmaxODmax": true,
      "odmaxODmax_segment": "[ 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2100.0, 2200.0, 2300.0, 2400.0, 2500.0, 2600.0, 2700.0, 2800.0, 2900.0, 3000.0, 3100.0, 3200.0, 3300.0, 3400.0, 3500.0, 3600.0, 3700.0, 3800.0, 3900.0, 4000.0, 4100.0, 4200.0, 4300.0, 4400.0, 4500.0, 4600.0, 4700.0, 4800.0, 4900.0, 5000.0, 5100.0, 5200.0, 5300.0, 5400.0, 5500.0, 5600.0, 5700.0, 5800.0, 5900.0, 6000.0, 6100.0, 6200.0, 6300.0, 6400.0, 6500.0, 6600.0, 6700.0, 6800.0, 6900.0, 7000.0, 7100.0, 7200.0, 7300.0, 7400.0, 7500.0, 7600.0, 7700.0, 7800.0, 7900.0, 8000.0, 8100.0, 8200.0, 8300.0, 8400.0, 8500.0, 8600.0, 8700.0, 8800.0, 8900.0, 9000.0, 9100.0, 9200.0, 9300.0, 9400.0, 9500.0, 9600.0, 9700.0, 9800.0, 9900.0, 10000.0, 10100.0, 10200.0, 10300.0, 10400.0, 10500.0, 10600.0, 10700.0, 10800.0, 10900.0, 11000.0, 11100.0, 11200.0, 11300.0, 11400.0, 11500.0, 11600.0, 11700.0, 11800, 11900, 12000, 12100, 12200, 12300, 12400]",
      "repeat_measurWTmin": false,
      "repeat_measurWTavg": false,
      "repeat_measurWTmax": false,
      "repeat_measurODmin": false,
      "repeat_measurODavg": false,
      "repeat_measurODmax": false,
      "ab_ovov": false,
      "ab_ovov_segment": null,
      "ab_eccecc": false,
      "ab_eccecc_segment": null,
      "ab_WTminWTmin": false,
      "ab_WTminWTmin_segment": null,
      "max_pitch_OD": false,
      "max_pitch_WT": false
    }
    ```

    - platforma
    ```json
      {
        "duplic_inspec_OD": false,
        "duplic_inspec_WT": false,
        "empty_values_ODODmin": false,
        "empty_values_ODODavg": false,
        "empty_values_ODODmax": false,
        "empty_values_WTWTmin": false,
        "empty_values_WTWTavg": false,
        "empty_values_WTWTmax": false,
        "short_pipe": false,
        "long_pipe": true,
        "wtminWTmin": false,
        "wtminWTmin_segment": null,
        "odminODmin": false,
        "odminODmin_segment": null,
        "odmaxODmax": true,
        "odmaxODmax_segment": "[600.0,700.0,800.0,900.0,1000.0,1100.0,1200.0,1300.0,1400.0,1500.0,1600.0,1700.0,1800.0,1900.0,2000.0,2100.0,2200.0,2300.0,2400.0,2500.0,2600.0,2700.0,2800.0,2900.0,3000.0,3100.0,3200.0,3300.0,3400.0,3500.0,3600.0,3700.0,3800.0,3900.0,4000.0,4100.0,4200.0,4300.0,4400.0,4500.0,4600.0,4700.0,4800.0,4900.0,5000.0,5100.0,5200.0,5300.0,5400.0,5500.0,5600.0,5700.0,5800.0,5900.0,6000.0,6100.0,6200.0,6300.0,6400.0,6500.0,6600.0,6700.0,6800.0,6900.0,7000.0,7100.0,7200.0,7300.0,7400.0,7500.0,7600.0,7700.0,7800.0,7900.0,8000.0,8100.0,8200.0,8300.0,8400.0,8500.0,8600.0,8700.0,8800.0,8900.0,9000.0,9100.0,9200.0,9300.0,9400.0,9500.0,9600.0,9700.0,9800.0,9900.0,10000.0,10100.0,10200.0,10300.0,10400.0,10500.0,10600.0,10700.0,10800.0,10900.0,11000.0,11100.0,11200.0,11300.0,11400.0,11500.0,11600.0,11700.0,11800.0,11900.0,12000.0,12100.0,12200.0,12300.0,12400.0,12500.0]",
        "repeat_measurWTmin": false,
        "repeat_measurWTavg": false,
        "repeat_measurWTmax": false,
        "repeat_measurODmin": false,
        "repeat_measurODavg": false,
        "repeat_measurODmax": false,
        "ab_ovov": false,
        "ab_ovov_segment": null,
        "ab_eccecc": false,
        "ab_eccecc_segment": null,
        "ab_WTminWTmin": false,
        "ab_WTminWTmin_segment": null,
        "max_pitch_OD": false,
        "max_pitch_WT": false
      }
    ```

  - DB2398 XX 5

    não tem no original

  - DB2398 XX 17

    não tem no original

  - DB2398 XX 32

    não tem no original

- #### Comparativo de valores
  - DB2397 XX 31
    ![original_31](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_o_31.png?raw=true)

    ![platform_31](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_p_31.png?raw=true)

  - DB2397 XX 22
    ![original_22](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_o_22.png?raw=true)

    ![platform_22](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_p_22.png?raw=true)

  - DB2399 XX 54
    ![original_54](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_o_54.png?raw=true)

    ![platform_54](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_p_54.png?raw=true)

  - DB2398 XX 5
    - não gerado no original

    ![platform_5](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_p_5.png?raw=true)

  - DB2398 XX 17
    - não gerado no original

    ![platform_17](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/v_p_p_17.png?raw=true)

  
### Execução do modelo de colapso

1. Rodar o modelo de colapso com valores sugeridos na versão original

- [collapse_data_aramis_original.xlsx](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/collapse_data_aramis_original.xlsx)

2. Executar o valor de colapso com os mesmo parâmetros de entrada na plataforma

- [collapse_platform.csv](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/collapse_platform.csv)

3. Comparar valores de colapso de saída original vs plataforma
   
  ![comparativo_collapse](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/comparativo_collapse.png?raw=true)

### Executar as mesmas etapas anteriores com os arquivos vstar

- [119098_14inch_VM125HC_compiled_wt.xlsx](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/119098_14inch_VM125HC_compiled_wt.xlsx)

- [119098_14inch_VM125HC_compiled_od.xlsx](https://github.com/alorenacunha/docs-public/blob/main/collapse_validation/119098_14inch_VM125HC_compiled_od.xlsx)

1. Ler arquivos nos códigos 'original' versão do Versiani e executar o verify_pipe realizando as conversões de unidade

- Não conseguimos rodar o arquivo no código original para validação. Esta dando erro na leitura e tipagem do arquivo
