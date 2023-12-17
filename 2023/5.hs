-- Day 5: If You Give A Seed A Fertilizer
import Data.List
main :: IO()
main = do
 input <- getContents
 let almanac :: [String] = lines input

 let seeds :: [Integer] = [read x :: Integer | x <- drop 1 . words $ head almanac]
 let maps :: [[[Integer]]] = split_maps $ tail almanac

 putStrLn . show $ solve_1 seeds maps
 putStrLn . show $ solve_2 seeds maps

 where 
  split_maps :: [String] -> [[[Integer]]]
  split_maps ss = map format_map $ groupBy (\x y -> (x == "") && (y /= "")) ss
   where
    format_map :: [String] -> [[Integer]]
    format_map ss = map (\s -> [read x :: Integer | x <- words s]) $ drop 2 ss


solve_1 :: [Integer] -> [[[Integer]]] -> Integer
solve_1 seeds maps = minimum $ map (\x -> get_location x maps) seeds
 where
  get_location :: Integer -> [[[Integer]]] -> Integer
  get_location n [] = n
  get_location n (m:ms) = get_location (map_seed n m) ms
   where
    map_seed :: Integer -> [[Integer]] -> Integer
    map_seed n [] = n
    map_seed n (m:ms) =
     if (0 <= idx && idx < last m)
     then head m + idx
     else map_seed n ms
     where
      src_start :: Integer = m!!1
      idx :: Integer = n - src_start


solve_2 :: [Integer] -> [[[Integer]]] -> Integer
solve_2 seed_ranges maps = -1
