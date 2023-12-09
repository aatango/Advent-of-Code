-- Day 2: Cube Conundrum
import Data.List

-- Part One

-- Bag limits
max_red :: Integer = 12
max_blue :: Integer = 14
max_green :: Integer = 13

find_all :: [String] -> String -> [Int]
find_all game colour = map (\x -> x - 1) $ findIndices (isPrefixOf colour) game

draw_colour :: [String] -> String -> [Integer]
draw_colour game colour = [read x :: Integer | x <- map (game!!) $ find_all game colour]

validate_drawn_colour :: [String] -> String -> Integer -> Bool
validate_drawn_colour game colour max = all (<= max) $ draw_colour game colour

validate_game :: String -> Bool
validate_game game = validate_drawn_colour (words game) "red" max_red &&
                     validate_drawn_colour (words game) "blue" max_blue &&
                     validate_drawn_colour (words game) "green" max_green

solve_1 :: [String] -> Int
solve_1 games = sum $ map (\x -> x + 1) $ findIndices validate_game games


-- Part Two

find_max_colour :: [String] -> String -> Integer
find_max_colour game colour = maximum $ draw_colour game colour

calculate_game_power :: String -> Integer
calculate_game_power game = product $ find_max_colour (words game) "red" :
                                      find_max_colour (words game) "blue" :
                                      find_max_colour (words game) "green": []

solve_2 :: [String] -> Integer
solve_2 games = sum $ map calculate_game_power games

main :: IO()
main = do
 input <- getContents
 let games :: [String] = lines input

 putStrLn . show $ solve_1 games
 putStrLn . show $ solve_2 games
