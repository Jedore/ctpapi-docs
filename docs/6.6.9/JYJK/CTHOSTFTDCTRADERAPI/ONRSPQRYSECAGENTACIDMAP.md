<p>请求查询二级代理操作员银期权限响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSECAGENTACIDMAP/">ReqQrySecAgentACIDMap</a>后，该方法被调用。</p>
<span class="anchor" id="050b6eab-9e7f-4e41-afda-113f89767521"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="07d501ce-2953-4533-a965-3d17be3814ae"></span>
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
<span class="anchor" id="41a2c5a5-a3f0-4e0e-9a8a-ad5f65684d3e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="75da27e8-8df9-4c37-8e66-f0510f241a09"></span>
## 4.FAQ
<p>无</p>
