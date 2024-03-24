<p>登出请求响应，当ReqUserLogout后，该方法被调用。</p>
<span class="anchor" id="8faa65fa-f603-4ce1-9f60-9dff177ddd72"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="aae6d9b6-153f-45c6-953f-d26bde9e34c6"></span>
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
<span class="anchor" id="e7c05dbf-baba-444c-b595-870b08254544"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b4719f1c-5409-4f76-975f-6f6a06e9603d"></span>
## 4.FAQ
<p>无</p>
