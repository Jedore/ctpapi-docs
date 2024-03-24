<p>请求查询投资单元响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTUNIT/">ReqQryInvestUnit</a>后，该方法被调用。</p>
<span class="anchor" id="2a06a2e7-d60c-4e2f-9340-17153e1a8d7d"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f2fe33ed-83e5-4868-93aa-75da4160fb41"></span>
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
<span class="anchor" id="148b09e7-3d82-4e38-a188-bb663046beb7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1d97f2d4-2bdc-4a8d-b9e8-8ed2bbd6b81f"></span>
## 4.FAQ
<p>无</p>
