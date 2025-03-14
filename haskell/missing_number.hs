findMissing :: [Int] -> Int -> Int
findMissing nums n = (n * (n + 1) `div` 2) - sum nums

main :: IO()
main = do
    n <- readLn
    nums <- fmap (map read . words) getLine
    print $ findMissing nums n
