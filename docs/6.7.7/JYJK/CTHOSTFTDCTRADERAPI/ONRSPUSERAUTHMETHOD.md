<p>查询用户当前支持的认证模式的回复</p>
<span class="anchor" id="3ff83bb1-79aa-4ef3-9ae8-fc21fe3ee53a"></span>
## 1.函数原型
<p>virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="339c44d2-5ad6-4cdf-b2e8-75569f125df1"></span>
## 2.参数
<p>pRspUserAuthMethod：用户发出获取安全安全登陆方法回复</p>
<pre><code>struct CThostFtdcRspUserAuthMethodField
{
    ///当前可以用的认证模式
    TThostFtdcCurrentAuthMethodType UsableAuthMethod;
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
<span class="anchor" id="06385ab5-11e9-41c0-80fd-c774f5281530"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ac2c52a2-bb3a-417d-9c3f-2172cdc897f1"></span>
## 4.FAQ
<p>无</p>
