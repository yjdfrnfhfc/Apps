import vk_api

def main():

    login, password = '380502075035', 'green_grass'

    try:
        vk = vk_api.VkApi(login, password)
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return
    cnt=1
    ofs=0
    rsb_ids=[]
    values = {'group_id': 'rsbua', 'count':cnt, 'offset': ofs}
    response = vk.method('groups.getMembers', values)

    if response['count']:
        rsb_count=response['count']
        print(rsb_count)
        while ofs<min(1,rsb_count-cnt):
            
            values = {'group_id': 'rsbua', 'count':cnt, 'offset': ofs}
            response = vk.method('groups.getMembers', values)
##            while cnt>0:
##                print(response['items'][ofs+cnt], cnt, ofs)
##                cnt-=1

            ofs=ofs+cnt

            rsb_ids+=response['items']
            print(cnt, ofs, response['items'])
            
##        cnt=rsb_count-ofs
##        values = {'group_id': 'rsbua', 'count':cnt, 'offset': ofs}
##        response = vk.method('groups.getMembers', values)
##        rsb_ids+=response['items']
##        print(len(rsb_ids))
##        while cnt>0:
##            print(response['items'][ofs+cnt],':', cnt, ofs)

if __name__=='__main__':
    main()
