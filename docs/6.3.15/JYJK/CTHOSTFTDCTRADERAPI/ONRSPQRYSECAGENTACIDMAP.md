<p>请求查询二级代理操作员银期权限响应，当执行ReqQrySecAgentACIDMap后，该方法被调用。</p>
<span class="anchor" id="5326407d-59ec-4a0b-909b-a5723c591bef"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="18ae5872-61ca-46f2-8c1c-3952f24d1db2"></span>
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
<span class="anchor" id="cc10c850-ee6f-4ec4-a60e-0f8d7aa11beb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ec58f22f-4289-4b81-a65f-3163f3c75d49"></span>
## 4.FAQ
<p>无</p>
