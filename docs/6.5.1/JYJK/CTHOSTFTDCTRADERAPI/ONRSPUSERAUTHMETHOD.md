<p>查询用户当前支持的认证模式的回复</p>
<span class="anchor" id="0132808c-061a-4063-b6b4-45afbef4d9e2"></span>
## 1.函数原型
<p>virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="515e06fc-8424-48be-afe6-625f2ac4fff2"></span>
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
<span class="anchor" id="79a11f3d-895b-488e-b188-3dad4e94533a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="56ad9dc0-9a78-4245-aadf-14e614f85aaf"></span>
## 4.FAQ
<p>无</p>
