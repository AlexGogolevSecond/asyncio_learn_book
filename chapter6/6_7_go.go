package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

func main() {
	// Получаем домашнюю директорию пользователя
	homeDir, err := os.UserHomeDir()
	if err != nil {
		log.Fatalf("Ошибка получения домашней директории: %v", err)
	}

	// Формируем полный путь к файлу
	filePath := filepath.Join(homeDir, "py_tmp", "asyncio_learn_book", "chapter6", "googlebooks-eng-all-1gram-20120701-a")
	fmt.Printf("Ищем файл по пути: %s\n", filePath)

	// Получение размера файла
	fileInfo, err := os.Stat(filePath)
	if err != nil {
		log.Fatalf("Ошибка получения информации о файле: %v\nПроверьте:\n1. Существует ли файл\n2. Правильно ли указан путь\n3. Распакован ли архив", err)
	}

	fileSize := fileInfo.Size()
	fmt.Printf("Размер файла: %d байт (%.2f Гбайт)\n", fileSize, float64(fileSize)/(1024*1024*1024))

	startTotal := time.Now()
	freqs := make(map[string]int)

	// Открытие файла
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Ошибка открытия файла: %v", err)
	}
	defer file.Close()

	startProcessing := time.Now()
	scanner := bufio.NewScanner(file)
	lineCount := 0

	// Увеличиваем буфер сканера для больших строк
	const maxCapacity = 1024 * 1024 * 10 // 10MB
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, "\t")
		if len(parts) < 3 {
			continue
		}

		word := parts[0]
		count, err := strconv.Atoi(parts[2])
		if err != nil {
			continue
		}

		freqs[word] += count
		lineCount++

		// Вывод прогресса каждые 5 миллионов строк
		if lineCount%5000000 == 0 {
			fmt.Printf("Обработано %d млн строк\n", lineCount/1000000)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Ошибка при сканировании файла: %v", err)
	}

	elapsedProcessing := time.Since(startProcessing)
	elapsedTotal := time.Since(startTotal)

	fmt.Printf("Обработка завершена. Всего строк: %d\n", lineCount)
	fmt.Printf("Время обработки: %.2f сек.\n", elapsedProcessing.Seconds())
	fmt.Printf("Общее время выполнения: %.2f сек.\n", elapsedTotal.Seconds())
	fmt.Printf("Уникальных слов: %d\n", len(freqs))
}