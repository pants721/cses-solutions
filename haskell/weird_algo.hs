solve :: Integer -> [Integer]
solve 1 = [1]
solve n
    | even n = n : solve (n `div` 2)
    | otherwise = n : solve (3 * n + 1)

main :: IO ()
main = do
    n <- readLn
    putStrLn . unwords . map show $ solve n
