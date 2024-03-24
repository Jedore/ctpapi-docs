<p>登出请求响应，当ReqUserLogout后，该方法被调用。</p>
<span class="anchor" id="d383665e-632a-4ea6-9cb3-2f7195b93e17"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="91df2e47-ccd7-4bc0-92d3-6df503a0de80"></span>
## 2.参数
<p>pUserLogout：用户登出请求</p>
<pre><code>struct CThostFtdcUserLogoutField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
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
<p>nRequestID：返回用户操作请求的ID，该ID由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="917a3af7-c2ef-46a7-926f-e63e2a644bcc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0bc91062-3e4d-416e-a652-3cdae6185d0b"></span>
## 4.FAQ
<p>无</p>
