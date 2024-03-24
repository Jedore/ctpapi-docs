<p>登出请求响应，当执行ReqUserLogout后，该方法被调用。</p>
<span class="anchor" id="5b9e196f-350a-4d50-8d9a-2f1e21070fec"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2f30ec0c-aafb-4379-8c59-37fe1d7edfdd"></span>
## 2.参数
<p>pUserLogout:用户登出请求</p>
<pre><code>struct CThostFtdcUserLogoutField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
};
</code></pre>
<p>pRspInfo:响应信息</p>
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
<span class="anchor" id="1b8ca119-8329-467e-9d14-560922110e4b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="94150bb6-7bc3-4753-b01a-202b33180d69"></span>
## 4.FAQ
<p>无</p>
