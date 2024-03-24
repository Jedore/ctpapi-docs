<p>登出请求响应，当ReqUserLogout后，该方法被调用。</p>
<span class="anchor" id="91346755-7796-4462-8a33-549130f94994"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="aa0bf513-a380-4cab-b069-94d4d3b18211"></span>
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
<span class="anchor" id="49a125d3-53f5-41aa-9db4-475b20771bcf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="54783718-ee92-4bb8-aea2-bc66b9a8dab0"></span>
## 4.FAQ
<p>无</p>
