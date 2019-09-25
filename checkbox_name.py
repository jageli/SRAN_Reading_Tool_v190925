checkbox_name = ['MRBTS','HW', 'GNSSE_R','GNSSE_HW','GNBCF','GNCEL','GNCEL_R','LNBTS','LNCEL','LNCEL_FDD','NBIOT_FDD',
                 'VLANIF','IPADDRESSV4','IPRT','MPLANENW','BBMOD_HW','SMOD_HW','RMOD_HW','BBMOD_R','SMOD_R','RMOD_R',
                 'LNMME','CHANNEL','CARRIERGROUPC_R','MNL_R','CHANNELGROUP','SECADM','FEATCADM','BBMOD_EQM','SMOD_EQM',
                 'RMOD_EQM','GNSSE_MNL','ANTL_R','TIME1','UNIT','HW_GSM','LNCEL_TDD','IPNO','CLOCK','SFP_R','IVIF','ASIRMOD_R','LCELL','SYNC','CABLINK_R']


def list():
    node_list = []
    x = 0
    for x in range(len(checkbox_name)):
        node_list.append([])
    return node_list




