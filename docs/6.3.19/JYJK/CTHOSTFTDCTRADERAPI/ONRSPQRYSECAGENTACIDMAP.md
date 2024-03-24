<p>请求查询二级代理操作员银期权限响应，当执行ReqQrySecAgentACIDMap后，该方法被调用。</p>
<span class="anchor" id="6b213270-653c-4dfa-86e9-5e227d1eefd3"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f24545cd-7092-4468-9ba7-5ae67447ff31"></span>
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
<span class="anchor" id="d3e31ba7-8524-402d-a3d7-eee5d191ebc5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0ff1f989-483c-41be-94d6-738be9acabf2"></span>
## 4.FAQ
<p>无</p>
