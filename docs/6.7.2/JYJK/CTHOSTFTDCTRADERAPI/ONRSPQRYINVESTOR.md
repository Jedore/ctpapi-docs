<p>请求查询投资者响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTOR/">ReqQryInvestor</a>后，该方法被调用。</p>
<span class="anchor" id="766481f1-f9be-4355-98c9-50672800f342"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="20de26a1-cc02-433b-b097-55b4620b7fbc"></span>
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
    ///是否频率控制
    TThostFtdcEnumBoolType  IsOrderFreq;
    ///是否开仓限制
    TThostFtdcEnumBoolType  IsOpenVolLimit;
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
<span class="anchor" id="786490a8-b7c5-40d1-8e01-30d3a78428cb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2d70b39e-ba35-41e5-a248-ad28350dcd57"></span>
## 4.FAQ
<p>无</p>
