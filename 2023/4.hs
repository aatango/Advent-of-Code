-- Day 4: Scratchcards

import Data.List

to_integers :: [String] -> [Integer]
to_integers ss = [read x :: Integer | x <- ss]

-- `drop 2` to remove "Card {NUMBER}:"
split :: String -> ([String], [String])
split card = span (/="|") (drop 2 $ words card)

winning_numbers :: String -> [Integer]
winning_numbers card = to_integers . fst $ split card

-- `tail` to remove the character '|' from the beginning of the list
your_numbers :: String -> [Integer]
your_numbers card = to_integers . tail . snd $ split card

matching_numbers :: String -> [Integer]
matching_numbers card = filter (\x -> elem x yours) winning
 where
  yours :: [Integer] = your_numbers card
  winning :: [Integer] = winning_numbers card 

-- Part One

number_of_matches :: String -> Integer
number_of_matches card = toInteger $ length your_winning_numbers
 where your_winning_numbers :: [Integer] = matching_numbers card

solve_1 :: [String] -> Integer
solve_1 [] = 0
solve_1 (x:xs) = div (2 ^ (number_of_matches x)) 2 + solve_1 xs

-- Part Two
solve_2 :: [String] -> Integer
solve_2 x = -1


main :: IO()
main = do
 input <- getContents
 let cards :: [String] = lines input

 putStrLn . show $ solve_1 cards
 putStrLn . show $ solve_2 cards
