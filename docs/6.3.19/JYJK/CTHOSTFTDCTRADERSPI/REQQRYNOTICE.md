<p>请求查询客户通知</p>
<p>响应: OnRspQryNotice</p>
<span class="anchor" id="1118e4eb-5c8c-4e70-a389-27907a1bd2f6"></span>
## 1.函数原型
<p>virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;</p>
<span class="anchor" id="c7130b13-b44e-4f25-b0c0-62edba7f9f15"></span>
## 2.参数
<p>pQryNotice：查询客户通知</p>
<pre><code>struct CThostFtdcQryNoticeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="616a6667-d405-4566-b9fd-20e0d0e086b2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2964bda3-a5d1-45d2-94dc-804f445910dd"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6e44e53d-c9ea-472f-a858-882b4ae56088"></span>
## 5.FAQ
<p>无</p>
