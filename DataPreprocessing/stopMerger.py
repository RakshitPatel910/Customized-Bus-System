import stopLatLongMerge as sllm

pathInfo = [
    # {
    #     'path' : '../dataset/clean_data/700.csv',
    #     'routeNo' : '700'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/701.csv',
    #     'routeNo' : '701'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/702.csv',
    #     'routeNo' : '702'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/703.csv',
    #     'routeNo' : '703'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/705.csv',
    #     'routeNo' : '705'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/706.csv',
    #     'routeNo' : '706'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/707.csv',
    #     'routeNo' : '707'
    # },
    {
        'path' : '../dataset/clean_data/709.csv',
        'routeNo' : '709'
    },
    # {
    #     'path' : '../dataset/RouteFootfall/710.csv',
    #     'routeNo' : '710'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/718.csv',
    #     'routeNo' : '718'
    # },
    # {
    #     'path' : '../dataset/RouteFootfall/720.csv',
    #     'routeNo' : '720'
    # },
]

for x in pathInfo:
    sllm.merge(x)