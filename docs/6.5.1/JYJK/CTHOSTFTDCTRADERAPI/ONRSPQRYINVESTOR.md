<p>请求查询投资者响应，当执行ReqQryInvestor后，该方法被调用。</p>
<span class="anchor" id="a5873999-0194-479f-8476-cbf3902ed648"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="82c4663f-e2b9-4ef6-bd74-0e9b24e9d724"></span>
## 2.参数
<p>pInvestor：投资者</p>
<pre><code>struct CThostFtdcInvestorField
{
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者分组代码
    TThostFtdcInvestorIDType InvestorGroupID;
    ///投资者名称
    TThostFtdcPartyNameType InvestorName;
    ///证件类型
    TThostFtdcIdCardTypeType IdentifiedCardType;
    ///证件号码
    TThostFtdcIdentifiedCardNoType IdentifiedCardNo;
    ///是否活跃
    TThostFtdcBoolType IsActive;
    ///联系电话
    TThostFtdcTelephoneType Telephone;
    ///通讯地址
    TThostFtdcAddressType Address;
    ///开户日期
    TThostFtdcDateType OpenDate;
    ///手机
    TThostFtdcMobileType Mobile;
    ///手续费率模板代码
    TThostFtdcInvestorIDType CommModelID;
    ///保证金率模板代码
    TThostFtdcInvestorIDType MarginModelID;
};
</code></pre>
<p>CommModelID：CTP内部使用</p>
<p>MarginModelID：CTP内部使用</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="0d762eb5-ea10-46f8-9089-977c189e788d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8e8fba34-7d23-48b4-9ac0-764940115334"></span>
## 4.FAQ
<p>无</p>
