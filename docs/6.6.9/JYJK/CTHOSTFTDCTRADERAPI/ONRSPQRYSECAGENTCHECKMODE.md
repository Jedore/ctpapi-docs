<p>请求查询二级代理商资金校验模式响应</p>
<span class="anchor" id="eb7fb2f0-9248-42c5-89a1-c50aea0ac491"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="31368d13-423e-4b95-ae39-3cf41f660b74"></span>
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
<span class="anchor" id="e6b41184-7faa-44cb-86a8-add5beba0a59"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3f6962cd-3498-4492-87f7-599228e125e3"></span>
## 4.FAQ
<p>无</p>
