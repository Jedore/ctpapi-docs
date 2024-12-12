<p>请求查询二级代理操作员银期权限响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSECAGENTACIDMAP/">ReqQrySecAgentACIDMap</a>后，该方法被调用。</p>
<span class="anchor" id="77cad65c-c507-4f34-a851-88fc7a01929f"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="54f5b125-275f-4683-9fd3-1467c564bf90"></span>
## 2.参数
<p>pSecAgentACIDMap：二级代理操作员银期权限</p>
<pre><code>struct CThostFtdcSecAgentACIDMapField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///资金账户
    TThostFtdcAccountIDType AccountID;
    ///币种
    TThostFtdcCurrencyIDType CurrencyID;
    ///境外中介机构资金帐号
    TThostFtdcAccountIDType BrokerSecAgentID;
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
<span class="anchor" id="1055bdbb-d2de-4d92-8b4c-af5e54382075"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="094a5c7c-294a-4f1c-b177-657690ef37e2"></span>
## 4.FAQ
<p>无</p>
