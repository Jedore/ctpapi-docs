<p>登出请求响应，当执行<a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGOUT/">ReqUserLogout</a>后，该方法被调用。</p>
<span class="anchor" id="72f58fca-840e-4f89-b8e5-c6f2270afc4e"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="42232e05-8cad-4099-9c6f-735b1c32b899"></span>
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
<span class="anchor" id="faaabbc2-3ce4-49ef-a369-a6364f32aec5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4e9e4466-efae-44ab-8291-58005bf81633"></span>
## 4.FAQ
<p>无</p>
