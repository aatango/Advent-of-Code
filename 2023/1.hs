-- Day 1: Trebuchet?

-- Part One
import Data.Char

extract_digits :: String -> String
extract_digits s = filter isDigit s

decode_calibration :: String -> Integer
decode_calibration s = read [head $ extract_digits s, last $ extract_digits s] :: Integer

solve_1 :: [String] -> Integer
solve_1 ss = sum $ map decode_calibration ss


-- Part Two
solve_2 :: [String] -> [String]
solve_2 ss = ss

main :: IO()
main = do
 input <- getContents
 let notes :: [String] = lines input

 putStrLn . show $ solve_1 notes
-- putStrLn . show $ solve_1 $ solve_2 notes
