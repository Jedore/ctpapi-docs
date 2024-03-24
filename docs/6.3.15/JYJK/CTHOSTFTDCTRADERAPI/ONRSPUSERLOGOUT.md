<p>登出请求响应，当执行ReqUserLogout后，该方法被调用。</p>
<span class="anchor" id="9e58f8fe-f6af-454a-8cca-c08ac5f6b314"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="930268cc-2165-4fbe-af24-5526adcff168"></span>
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
<span class="anchor" id="1c524e01-7dc7-41b9-9672-b3cc670c4c90"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a4898195-8884-49ca-97b6-d1b6398c8725"></span>
## 4.FAQ
<p>无</p>
