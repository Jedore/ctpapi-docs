<p>请求查询投资单元响应，当执行ReqQryInvestUnit后，该方法被调用。</p>
<span class="anchor" id="c48b47b3-ddb2-4afa-a9d9-b9ac68b28966"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5bd49dfa-9a7b-4034-a46d-51fc2eb4e583"></span>
## 2.参数
<p>pInvestUnit：投资单元</p>
<pre><code>struct CThostFtdcInvestUnitField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///投资者单元名称
    TThostFtdcPartyNameType InvestorUnitName;
    ///投资者分组代码
    TThostFtdcInvestorIDType InvestorGroupID;
    ///手续费率模板代码
    TThostFtdcInvestorIDType CommModelID;
    ///保证金率模板代码
    TThostFtdcInvestorIDType MarginModelID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
};
</code></pre>
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
<span class="anchor" id="3a49dbdc-b6e1-4e99-aa09-ef0a1c3dad55"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ac34aa33-5109-433b-bd7c-298c6c5402c8"></span>
## 4.FAQ
<p>无</p>
