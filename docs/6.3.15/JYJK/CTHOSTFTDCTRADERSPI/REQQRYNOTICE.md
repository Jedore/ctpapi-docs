<p>请求查询客户通知</p>
<p>响应: OnRspQryNotice</p>
<span class="anchor" id="daea28a4-f9f6-4407-89db-601d47f3e490"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="28596828-f757-48d0-b930-e9149f8a1ee0"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<pre><code>struct CThostFtdcQryNoticeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="aa369831-c913-4aef-b3b9-7a146338634d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b2f59d0a-a30c-4e23-9687-11fb04237470"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="7f422532-93d0-44e2-bcd3-d6d984a46856"></span>
## 5.FAQ
<p>无</p>
