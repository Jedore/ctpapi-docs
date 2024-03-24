<p>登出请求响应，当执行ReqUserLogout后，该方法被调用。</p>
<span class="anchor" id="e28f8090-0f96-4b98-8ced-c52ac0acfa09"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="cee460f5-022c-4e57-8ca0-b4f778960ec7"></span>
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
<span class="anchor" id="f48ed86f-d143-4fa8-88fe-29a5d5a2048a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b3d4e7c9-2e50-40c7-a6bb-d01cfd9aa828"></span>
## 4.FAQ
<p>无</p>
