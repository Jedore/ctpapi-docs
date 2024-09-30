<p>请求查询二级代理商资金校验模式响应</p>
<span class="anchor" id="5f91b9ee-fd47-4ffe-a2f6-95e409b934d5"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d2885b27-61db-428a-9a2f-7deda8f845ad"></span>
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
<span class="anchor" id="36d399d2-01e1-40cd-9999-9d53b290cedf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="39cfd06c-739d-470f-9acd-5e635d5fe9e0"></span>
## 4.FAQ
<p>无</p>
