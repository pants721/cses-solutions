import Data.List (group)
longest :: String -> Int
longest = maximum . map length . group

main :: IO()
main = print . longest =<< getLine
