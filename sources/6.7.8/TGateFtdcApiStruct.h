#if !defined(TGATE_FTDCSTRUCT_H)
#define TGATE_FTDCSTRUCT_H

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "TGateFtdcApiDataType.h"

///�����ַ��ѯ
struct CTGateFtdcQryTGIpAddrParamField
{
	///���͹�˾����
	TTGateFtdcBrokerIDType BrokerID;
	///�û�����
	TTGateFtdcUserIDType   UserID;
};

///�����ַ����
struct CTGateFtdcTGIpAddrParamField
{
	///���͹�˾����
	TTGateFtdcBrokerIDType	BrokerID;
	///�û�����
	TTGateFtdcUserIDType   UserID;
	///�����ַ
	TTGateFtdcIpAddrType	Address;
	///�������Ĵ���
	TTGateFtdcDRIdentityIDType	DRIdentityID;
	///������������
	TTGateFtdcDRIdentityNameType	DRIdentityName;
	///���׵�ַOR�����ַ
	TTGateFtdcAddrSrvModeType	AddrSrvMode;
	///��ַ�汾
	TTGateFtdcAddrVerType	AddrVer;
	///�����ַ���
	TTGateFtdcCommonIntType	AddrNo;
	///�����ַ����
	TTGateFtdcAddrNameType	AddrName;
	///�Ƿ��ǹ��ܵ�ַ
	TTGateFtdcBoolType	IsSM;
	///�Ƿ���������ַ
	TTGateFtdcBoolType	IsLocalAddr;
	///��ַ������Ϣ
	TTGateFtdcAddrRemarkType	Remark;
};

struct CTGateFtdcRspInfoField
{
	///�������
	TTGateFtdcErrorIDType	ErrorID;
	///������Ϣ
	TTGateFtdcErrorMsgType	ErrorMsg;
};

#endif