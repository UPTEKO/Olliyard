/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32l4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define TOGGLE_UI_Pin GPIO_PIN_0
#define TOGGLE_UI_GPIO_Port GPIOA
#define BUSY_UI_Pin GPIO_PIN_1
#define BUSY_UI_GPIO_Port GPIOA
#define RST_UI_Pin GPIO_PIN_2
#define RST_UI_GPIO_Port GPIOA
#define DC_UI_Pin GPIO_PIN_3
#define DC_UI_GPIO_Port GPIOA
#define SPI1_CS_UI_Pin GPIO_PIN_4
#define SPI1_CS_UI_GPIO_Port GPIOA
#define SPI1_SCK_UI_Pin GPIO_PIN_5
#define SPI1_SCK_UI_GPIO_Port GPIOA
#define I2C3_SCL_BMS_Pin GPIO_PIN_7
#define I2C3_SCL_BMS_GPIO_Port GPIOA
#define LED1_STATUS_Pin GPIO_PIN_0
#define LED1_STATUS_GPIO_Port GPIOB
#define LED2_STATUS_Pin GPIO_PIN_1
#define LED2_STATUS_GPIO_Port GPIOB
#define I2C1_SCL_BMS_Pin GPIO_PIN_9
#define I2C1_SCL_BMS_GPIO_Port GPIOA
#define I2C1_SDA_BMS_Pin GPIO_PIN_10
#define I2C1_SDA_BMS_GPIO_Port GPIOA
#define ALERT_BMS_Pin GPIO_PIN_11
#define ALERT_BMS_GPIO_Port GPIOA
#define BOOT_BMS_Pin GPIO_PIN_12
#define BOOT_BMS_GPIO_Port GPIOA
#define I2C3_SDA_BMS_Pin GPIO_PIN_4
#define I2C3_SDA_BMS_GPIO_Port GPIOB
#define SPI1_MOSI_UI_Pin GPIO_PIN_5
#define SPI1_MOSI_UI_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */