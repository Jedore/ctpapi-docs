<p>请求查询二级代理商资金校验模式响应</p>
<span class="anchor" id="463daa07-54c0-459a-a080-487287e8d65c"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b016eb22-79f8-4212-867a-b97daac61349"></span>
## 2.参数
<p>pSecAgentCheckMode：二级代理商资金校验模式</p>
<pre><code>struct CThostFtdcSecAgentCheckModeField
{
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///币种
    TThostFtdcCurrencyIDType CurrencyID;
    ///境外中介机构资金帐号
    TThostFtdcAccountIDType BrokerSecAgentID;
    ///是否需要校验自己的资金账户
    TThostFtdcBoolType CheckSelfAccount;
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
<span class="anchor" id="5a87d4a9-cf49-41cc-b3a9-b799380551de"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5cb3195c-5552-4599-af9d-f522093b7169"></span>
## 4.FAQ
<p>无</p>
