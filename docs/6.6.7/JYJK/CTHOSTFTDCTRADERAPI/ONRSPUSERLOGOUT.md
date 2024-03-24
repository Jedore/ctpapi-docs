<p>登出请求响应，当执行<a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGOUT/">ReqUserLogout</a>后，该方法被调用。</p>
<span class="anchor" id="68037423-e4f1-4305-acf0-e3265e8fb4ed"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="bfddf8f0-bc28-41de-b2a9-1b91349a35e2"></span>
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
<span class="anchor" id="23d7da5b-c4c1-40a3-829b-72342d0cc32b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="97feca8a-5b1f-47e2-98ec-c59f89f47be9"></span>
## 4.FAQ
<p>无</p>
