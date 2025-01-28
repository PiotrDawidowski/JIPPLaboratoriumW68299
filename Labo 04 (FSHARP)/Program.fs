open System

// Zadanie 1

//type Uzytkownik = {
//    Waga: float
//    Wzrost: float
//    BMI: float
//    Kategoria: string
//}

//Console.WriteLine("Podaj swoją wagę: ")
//let waga = Console.ReadLine() |> float // przekazanie wagi w string do float
//Console.WriteLine("Podaj swój wzrost: ")
//let wzrost = Console.ReadLine() |> float |> (fun x -> x / 100.0)
//let bmi = waga / (wzrost * wzrost) // obliczenie BMI

//let obliczKategorie bmi = // bmi to argument funkcji
//    if bmi < 18.5 then "Niedowaga"
//    elif bmi >= 18.5 && bmi < 25.0 then "Waga prawidłowa"
//    elif bmi >= 25.0 && bmi < 30.0 then "Nadwaga"
//    else "Otyłość"

//let kategoria = obliczKategorie bmi

//let daneUzytkownika = {
//    Waga = waga
//    Wzrost = wzrost
//    BMI = bmi
//    Kategoria = kategoria
//   }

//Console.WriteLine("Twoje BMI i kategoria: ")
//printfn "BMI: %f, Kategoria: %s" daneUzytkownika.BMI daneUzytkownika.Kategoria

// Zadanie 2

//let exchangeRates = 
//    Map [
//        ("PLN", 1.0)
//        ("USD", 4.0)   // 1 USD = 4.0 PLN
//        ("EUR", 4.5)   // 1 EUR = 4.5 PLN
//        ("GBP", 5.2)   // 1 GBP = 5.2 PLN
//    ]

//let konwertujWalute amount fromCurrency toCurrency =
//    match Map.tryFind fromCurrency exchangeRates, Map.tryFind toCurrency exchangeRates with
//    | Some fromRate, Some toRate -> 
//        let convertedAmount = amount * (fromRate / toRate)
//        Some convertedAmount
//    | _ -> None

//Console.Write("Podaj kwotę do przeliczenia: ")
//let amount = Console.ReadLine() |> float

//Console.Write("Podaj walutę źródłową (USD, EUR, GBP, PLN): ")
//let fromCurrency = Console.ReadLine().ToUpper()

//Console.Write("Podaj walutę docelową (USD, EUR, GBP, PLN): ")
//let toCurrency = Console.ReadLine().ToUpper()

//match konwertujWalute amount fromCurrency toCurrency with
//| Some result -> printfn "Przeliczona kwota: %.2f %s" result toCurrency
//| None -> printfn "Błąd: Nieznana waluta!"

// Zadanie 3

//let countWords (text: string) =
//    text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
//    |> Array.length

//let countCharactersWithoutSpaces (text: string) =
//    text.Replace(" ", "").Length

//let findMostFrequentWord (text: string) =
//    text.Split([|' '; '\t'; '\n'; '\r'; ','; '.'; ';'; ':'; '!'|], StringSplitOptions.RemoveEmptyEntries)
//    |> Array.map (fun word -> word.ToLower()) // Konwersja na małe litery
//    |> Array.groupBy id // Grupowanie tych samych słów
//    |> Array.map (fun (word, occurrences) -> word, Array.length occurrences) // Tworzenie par (słowo, liczba wystąpień)
//    |> Array.maxBy snd // Znajdź parę z największą liczbą wystąpień


//Console.WriteLine("Podaj tekst do analizy:")
//let userInput = Console.ReadLine()

//let wordCount = countWords userInput

//let characterCount = countCharactersWithoutSpaces userInput

//let mostFrequentWord, frequency = findMostFrequentWord userInput

//printfn "Liczba słów: %d" wordCount
//printfn "Liczba znaków (bez spacji): %d" characterCount
//printfn "Najczęściej występujące słowo: '%s' (wystąpień: %d)" mostFrequentWord frequency

// Zadanie 4

open System

type Account = {
    AccountNumber: string
    Balance: float
}

let mutable accounts: Map<string, Account> = Map.empty

let createAccount accountNumber =
    if accounts.ContainsKey(accountNumber) then
        printfn "Konto z numerem '%s' już istnieje!" accountNumber
    else
        let newAccount = { AccountNumber = accountNumber; Balance = 0.0 }
        accounts <- accounts.Add(accountNumber, newAccount)
        printfn "Konto '%s' zostało utworzone!" accountNumber

let deposit accountNumber amount =
    match accounts.TryFind(accountNumber) with
    | Some account ->
        if amount > 0.0 then
            let updatedAccount = { account with Balance = account.Balance + amount }
            accounts <- accounts.Add(accountNumber, updatedAccount)
            printfn "Wpłacono %.2f na konto '%s'. Nowe saldo: %.2f" amount accountNumber updatedAccount.Balance
        else
            printfn "Kwota depozytu musi być większa niż 0!"
    | None ->
        printfn "Konto z numerem '%s' nie istnieje!" accountNumber

let withdraw accountNumber amount =
    match accounts.TryFind(accountNumber) with
    | Some account ->
        if amount > 0.0 then
            if amount <= account.Balance then
                let updatedAccount = { account with Balance = account.Balance - amount }
                accounts <- accounts.Add(accountNumber, updatedAccount)
                printfn "Wypłacono %.2f z konta '%s'. Nowe saldo: %.2f" amount accountNumber updatedAccount.Balance
            else
                printfn "Brak wystarczających środków na koncie!"
        else
            printfn "Kwota wypłaty musi być większa niż 0!"
    | None ->
        printfn "Konto z numerem '%s' nie istnieje!" accountNumber

let checkBalance accountNumber =
    match accounts.TryFind(accountNumber) with
    | Some account ->
        printfn "Saldo konta '%s': %.2f" account.AccountNumber account.Balance
    | None ->
        printfn "Konto z numerem '%s' nie istnieje!" accountNumber

let displayMenu () =
    printfn "\n=== Menu Bankowe ==="
    printfn "1. Utwórz nowe konto"
    printfn "2. Depozytuj środki"
    printfn "3. Wypłać środki"
    printfn "4. Wyświetl saldo"
    printfn "5. Wyjście"
    printf "Wybierz opcję: "

let rec mainLoop () =
    displayMenu()
    match Console.ReadLine() with
    | "1" ->
        printf "Podaj numer konta: "
        let accountNumber = Console.ReadLine()
        createAccount accountNumber
        mainLoop()
    | "2" ->
        printf "Podaj numer konta: "
        let accountNumber = Console.ReadLine()
        printf "Podaj kwotę do wpłaty: "
        let amount = Console.ReadLine() |> float
        deposit accountNumber amount
        mainLoop()
    | "3" ->
        printf "Podaj numer konta: "
        let accountNumber = Console.ReadLine()
        printf "Podaj kwotę do wypłaty: "
        let amount = Console.ReadLine() |> float
        withdraw accountNumber amount
        mainLoop()
    | "4" ->
        printf "Podaj numer konta: "
        let accountNumber = Console.ReadLine()
        checkBalance accountNumber
        mainLoop()
    | "5" ->
        printfn "Dziękujemy za skorzystanie z aplikacji bankowej!"
    | _ ->
        printfn "Nieprawidłowa opcja, spróbuj ponownie."
        mainLoop()
mainLoop()