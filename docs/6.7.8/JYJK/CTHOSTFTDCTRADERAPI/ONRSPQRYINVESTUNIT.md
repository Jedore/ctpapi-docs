<p>请求查询投资单元响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTUNIT/">ReqQryInvestUnit</a>后，该方法被调用。</p>
<span class="anchor" id="09460cf9-a1a7-44c2-8181-e1c5cbb14eba"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="11bcbc35-888b-421b-8820-5bff1acb180b"></span>
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
<span class="anchor" id="7fdaa22c-d8d5-4376-8dde-f4a38ec217b2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b66f87b8-a440-4fd8-b705-0c539be14579"></span>
## 4.FAQ
<p>无</p>
