#if !defined(TGATE_FTDCAPI_H)
#define TGATE_FTDCAPI_H

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#if defined(TGAPI_IS_LIB) && defined(WIN32)
#ifdef LIB_TG_API_EXPORT
#define TG_API_EXPORT __declspec(dllexport)
#else
#define TG_API_EXPORT __declspec(dllimport)
#endif
#else
#define TG_API_EXPORT 
#endif

#include "TGateFtdcApiStruct.h"

class CTGateFtdcSpi
{
public:
	///����Ӧ��
	virtual void OnRspError(CTGateFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast) {};

	///�����ַ������ѯ��Ӧ
	virtual void OnRspQryTGIpAddrParam(CTGateFtdcTGIpAddrParamField* pTGIpAddrParam, CTGateFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast) {};
};


class TG_API_EXPORT CTGateFtdcApi
{
public:
	///����TGApi
	static CTGateFtdcApi* CreateTGateFtdcApi();

	///��ȡAPI�İ汾��Ϣ
	///@retrun ��ȡ���İ汾��
	static const char* GetApiVersion();

	///ɾ���ӿڶ�����
	///@remark ����ʹ�ñ��ӿڶ���ʱ,���øú���ɾ���ӿڶ���
	virtual void Release() = 0;

	///�ȴ��ӿ��߳̽�������
	///@return �߳��˳�����
	virtual int Join() = 0;

	///ע��TGATE�����ַ
	///@param pszTGAddress��TGATE�����ַ��
	///@remark �����ַ�ĸ�ʽΪ����protocol://ipaddress:port�����磺��tcp://127.0.0.1:17001���� 
	///@remark ��tcp��������Э�飬��127.0.0.1�������������ַ����17001������������˿ںš�
	virtual void RegisterTGAddr(char* pszTGAddress) = 0;

	///ע��ص��ӿ�
	///@param pSpi �����Իص��ӿ����ʵ��
	virtual void RegisterSpi(CTGateFtdcSpi* pSpi) = 0;

	///�����ַ������ѯ
	/// ����ֵ��
	/// -1����γ���
	/// -2��������;����
	/// -3������Ƶ������ 
	virtual int ReqQryTGIpAddrParam(CTGateFtdcQryTGIpAddrParamField* pQryTGIpAddrParamField,int nRequestID) = 0;

protected:
	~CTGateFtdcApi() {};
};
#endif