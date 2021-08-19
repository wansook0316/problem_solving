import Foundation

let chessSize = 8

func calcFillCount(_ board: [[String]], with color: String, other: String) -> Int {
    var count = 0
    let colorDic = [0: color, 1: other]
    
    for i in 0..<chessSize {
        for j in 0..<chessSize {
            let nowColor = colorDic[(i + j) % 2]!
            if board[i][j] != nowColor {
                count += 1
            }
        }
    }
    return count
}

func getMinimumFillCount(_ board: [[String]]) -> Int {
    let startWithBlackCount = calcFillCount(board, with: "B", other: "W")
    let startWithWhiteCount = calcFillCount(board, with: "W", other: "B")
    return min(startWithBlackCount, startWithWhiteCount)
}

func main() {
    // 좌상, 우하를 가져온다.
    // 해당 부분 체스판을 넣어서 계산을 수행한다.
    // min 값을 업데이트 한다.
    
    let seps = readLine()!.split(separator: " ").map { Int($0)! }
    let n = seps[0], m = seps[1]
    var board = [[String]]()
    for _ in 0..<n {
        board.append(readLine()!.map { String($0) })
    }
    
    var minFillCount = 50*50+1
    
    for i in 0...n-chessSize {
        for j in 0...m-chessSize {
            let sy = i, sx = j, ey = i+chessSize, ex = j+chessSize
            let slicedBoard = board[sy..<ey].map { Array($0[sx..<ex]) }
            let count = getMinimumFillCount(slicedBoard)
            minFillCount = min(minFillCount, count)
        }
    }
    
    print(minFillCount)
}
main()
