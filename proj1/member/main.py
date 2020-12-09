import proj1.member.mem_dao as dao
import proj1.member.mem_vo as vo
def main():
    d = dao.Dao('hr', 'hr', 'localhost:1521/xe', 'utf-8')
    print('전체검색')
    mems = d.selectAll()
    for m in mems:
        print(m)
    print('ddd 추가')
    d.insert(vo.Member('ddd', '111', 'named', 'ddd@email.com'))
    print('ddd 검색')
    m = d.select('ddd')
    print(m)
    print('ddd 수정')
    d.update(vo.Member('ddd', '1234', '', 'dddxxx@email.com'))
    m = d.select('ddd')
    print(m)
    print('ddd 삭제')
    d.delete('ddd')
    print('ddd 삭제 후 전체검색')
    mems = d.selectAll()
    for m in mems:
        print(m)

main()