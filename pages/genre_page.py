from urllib.parse import quote
from fastapi import Request
from nicegui import ui

def register_genre_page():

    @ui.page('/genre')
    def genre_page(request: Request):
        name = request.query_params.get('name', '학생')
        student_id = request.query_params.get('student_id', '000000')

        fields = [
            {
                'key': 'molecular',
                'num': '01',
                'title': '분자생물학 연구실',
                'desc': '유전자, 단백질, 세포 기능을 분석해 질병의 원리를 탐구합니다.',
                'tag': 'Molecular Biology',
            },
            {
                'key': 'immune',
                'num': '02',
                'title': '면역학 연구실',
                'desc': '면역세포, 항체, 염증 반응을 바탕으로 치료 전략을 설계합니다.',
                'tag': 'Immunology',
            },
            {
                'key': 'precision',
                'num': '03',
                'title': '유전체·정밀의학 연구실',
                'desc': '유전체와 임상 정보를 활용해 개인 맞춤형 진단과 치료를 설계합니다.',
                'tag': 'Precision Medicine',
            },
            {
                'key': 'regeneration',
                'num': '04',
                'title': '줄기세포·재생의학 연구실',
                'desc': '줄기세포, 오가노이드, 생체재료를 활용한 질환 모델과 치료를 연구합니다.',
                'tag': 'Regenerative Medicine',
            },
            {
                'key': 'biomaterial',
                'num': '05',
                'title': '바이오소재 연구실',
                'desc': '나노기술을 활용해 약물전달, 표적치료, 진단 기술을 탐구합니다.',
                'tag': 'Nanobiotechnology',
            },
            {
                'key': 'digital',
                'num': '06',
                'title': '디지털 헬스 연구실',
                'desc': '웨어러블 디지털 기기와 생체신호를 활용해 건강 상태를 분석합니다.',
                'tag': 'Digital Health',
            },
        ]

        with ui.column().classes('w-full min-h-screen bg-slate-50'):

            # 상단 헤더
            with ui.element('div').classes(
                'w-full min-h-[60px] flex flex-col sm:flex-row items-start sm:items-center '
                'justify-between gap-3 px-4 sm:px-8 py-4 sm:py-0 bg-white border-b border-slate-200'
            ):
                with ui.column().classes('gap-0'):
                    ui.label('AMPhST Research Library').classes(
                        'text-lg sm:text-xl font-bold text-slate-900'
                    )
                    ui.label('논문 기반 연구설계 미션 아카이브').classes(
                        'text-xs text-slate-400'
                    )

                with ui.row().classes('items-center gap-2 sm:gap-3 flex-wrap'):
                    ui.label(f'{name} · {student_id}').classes(
                        'text-sm text-slate-500'
                    )

                    ui.button(
                        '이전',
                        icon='arrow_back',
                        on_click=lambda: ui.navigate.to(
                            f'/class?name={quote(name)}&student_id={quote(student_id)}'
                        )
                    ).props('flat dense').classes(
                        'text-slate-500 text-sm'
                    )

                    ui.button(
                        '로그아웃',
                        icon='logout',
                        on_click=lambda: ui.navigate.to('/')
                    ).props('flat dense').classes(
                        'text-slate-500 text-sm'
                    )

            # 본문
            with ui.column().classes(
                'w-full px-4 sm:px-8 lg:px-10 py-6 sm:py-8'
            ):

                ui.label('SELECT RESEARCH FIELD').classes(
                    'text-xs font-semibold tracking-widest text-blue-500'
                )

                ui.label('연구 분야를 선택하세요').classes(
                    'text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2'
                )

                ui.label(
                    '관심 있는 연구 분야를 선택하면 기존 논문 기반 연구설계 미션으로 이동합니다.'
                ).classes(
                    'text-sm sm:text-base text-slate-500 mt-3'
                )

                # 연구 분야 목록
                with ui.column().classes('w-full gap-3 mt-7'):

                    for field in fields:
                        with ui.element('div').classes(
                            'w-full flex flex-col sm:flex-row sm:items-center sm:justify-between '
                            'gap-4 px-5 sm:px-6 py-4 rounded-2xl '
                            'bg-white border border-slate-100 shadow-sm '
                            'transition-all duration-300 hover:shadow-md hover:-translate-y-1 hover:border-blue-200'
                        ):

                            with ui.row().classes('items-start gap-4 w-full min-w-0'):
                                ui.label(field['num']).classes(
                                    'text-xl sm:text-2xl font-extrabold text-slate-300 w-[44px] sm:w-[54px] shrink-0'
                                )

                                with ui.column().classes('flex-1 min-w-0 gap-1'):
                                    with ui.row().classes('items-center gap-2 flex-wrap'):
                                        ui.label(field['title']).classes(
                                            'text-lg sm:text-xl font-bold text-slate-900'
                                        )

                                        ui.label(field['tag']).classes(
                                            'text-[10px] font-semibold text-blue-500 bg-blue-50 px-2 py-1 rounded-full'
                                        )

                                    ui.label(field['desc']).classes(
                                        'text-sm text-slate-500 mt-1'
                                    )

                            ui.button(
                                '입장',
                                icon='arrow_forward',
                                on_click=lambda f=field: ui.navigate.to(
                                    f"/missions?lab={f['key']}&name={quote(name)}&student_id={quote(student_id)}"
                                )
                            ).props('flat dense').classes(
                                'w-fit sm:ml-auto text-blue-600 font-semibold text-sm'
                            )